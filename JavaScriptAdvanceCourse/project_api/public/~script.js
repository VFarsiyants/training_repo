'use strict';

const API_URL = "http://localhost:3000/api/v1/";
// const API_URL = 'https://raw.githubusercontent.com/\
// GeekBrainsTutorial/online-store-api/master/responses/';

function send(onError, onSuccess, url, method = 'GET',
    data = '', headers = {}, timeout = 60000) {

    let xhr;

    if (window.XMLHttpRequest) {
        // Chrome, Mozilla, Opera, Safari
        xhr = new XMLHttpRequest();
    } else if (window.ActiveXObject) {
        // Internet Explorer
        xhr = new ActiveXObject("Microsoft.XMLHTTP");
    }

    xhr.timeout = timeout;

    xhr.ontimeout = onError;

    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            if (xhr.status < 400) {
                onSuccess(xhr.responseText)
            } else if (xhr.status >= 400) {
                onError(xhr.status)
            }
        }
    }

    xhr.open(method, url, true);

    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");

    xhr.send(data);
}

function getCounter() {
    let last = 0;

    return () => ++last;
}

const stackIDGenrator = getCounter()


class Good {
    constructor({ id, title, price }) {
        this.id = id;
        this.title = title;
        this.price = price;
    }

    getId() {
        return this.id;
    }

    getPrice() {
        return this.price;
    }

    getTitle() {
        return this.title;
    }
}

class GoodStack {
    constructor(good) {
        this.id = stackIDGenrator();
        this.good = good;
        this.count = 1;
    }

    getGoodId() {
        return this.good.id
    }

    getGood() {
        return this.good;
    }

    getCount() {
        return this.count;
    }

    getStackPrice() {
        return this.good.price * this.count;
    }

    add() {
        this.count++;
        return this.count;
    }

    remove() {
        this.count--;
        return this.count;
    }
}

class Cart {
    constructor() {
        this.list = []
        this.cartHTML = new CartRender(this)

        document.querySelector('.cart-button').addEventListener('click', event => {
            document.querySelector('.cart').classList.toggle('cart__active');
        })
    }

    fetchCart(user_id) {
        const querryData = { "id_user": user_id };
        const onError = (err) => alert('Can\'t load basket')
        const onSuccess = (response) => {
            const data = JSON.parse(response);
            if (!data.length) {
                return;
            }
            data.forEach(stack => {
                const cartStack = new GoodStack(new Good({
                    id: stack.id_product,
                    title: stack.product_name,
                    price: stack.price
                }));
                cartStack.count = stack.quantity;
                this.list.push(cartStack);
            })
            this.cartHTML.renderCart();
        }
        return new Promise((resolve, reject) =>
            send(reject, resolve, `${API_URL}cart`, undefined, querryData))
            .then((response) => onSuccess(response))
            .catch((error) => onError(error))
    }

    add(good) {
        const idx = this.list.findIndex((stack) => stack.getGoodId() == good.id)

        if (idx >= 0) {
            this.list[idx].add()
        } else {
            this.list.push(new GoodStack(good))
        }
        this.cartHTML.renderCart();
    }

    remove(id) {
        const queryData = JSON.stringify({
            "id_product": id,
        })
        const onSuccess = (response) => {
            const idx = this.list.findIndex((stack) => stack.getGoodId() == id)
            if (idx >= 0) {
                this.list[idx].remove()

                if (this.list[idx].getCount() <= 0) {
                    this.list.splice(idx, 1)
                }
            }
            this.cartHTML.renderCart();
        };
        const onError = (err) => alert('Something went wrong');
        send(onError, onSuccess, `${API_URL}cart/remove`,
            'POST', queryData);

    }
}

class Showcase {
    constructor(cart) {
        this.list = [];
        this.cart = cart;
        this.showcaseHTML = new ShowcaseRenderer(this)
    }

    _onSuccess(response) {
        const data = JSON.parse(response);
        data.forEach(product => {
            this.list.push(
                new Good({
                    id: product.id_product, title: product.product_name,
                    price: product.price
                })
            )
        })
        this.showcaseHTML.renderShowcase();
        let addButtons = document.querySelectorAll('.add-button')
        addButtons.forEach(button => button.addEventListener('click',
            (event) => {
                this.addToCart(event.target.dataset.product_id);
            }
        ))

        let removeButtons = document.querySelectorAll('.remove-button')
        removeButtons.forEach(button => button.addEventListener('click',
            (event) => this.cart.remove(event.target.dataset.product_id)
        ))
    }

    _onError(err) {
        console.log(err);
    }

    fetchGoods() {
        return new Promise((resolve, reject) => send(reject, resolve,
            `${API_URL}showcase`)).then((response) => this._onSuccess(response))
            .catch((error) => this._onError(error))
    }

    addToCart(id) {
        const queryData = JSON.stringify({
            "id_product": id,
            "quantity": 1
        })
        const onSuccess = (response) => {
            const idx = this.list.findIndex((good) => id == good.id)

            if (idx >= 0) {
                this.cart.add(this.list[idx])
            }
        };
        const onError = (err) => alert('Something went wrong');
        send(onError, onSuccess, `${API_URL}cart`, 'POST',
            queryData, { 'Content-Type': 'application/json;charset=UTF-8' });
    }
}

class GoodRenderer {
    constructor(good) {
        this.good = good;
    }

    renderGoodHTML() {
        return `<div class="goods-item"><div class="goods-item-image">
        </div><h3>${this.good.title}</h3><p>${this.good.price} Руб.</p><button \
        class="add-button" data-product_id="${this.good.id}" type="button">Add \
        to Cart</button><button class="remove-button" \
        data-product_id="${this.good.id}" type="button">Remove \
        from Cart</button></div>`
    }
}

class ShowcaseRenderer {
    constructor(showcase) {
        this.goodsList = showcase.list
    }

    renderShowcase() {
        // insertion of products divs
        let goodsList = showcase.list.map(item => new GoodRenderer(item));
        document.querySelector('.goods-list').innerHTML = goodsList
            .map(item => item.renderGoodHTML()).join('');
    }
}

class GoodInCartRenderer {
    constructor(goodStack) {
        this.goodStackInCart = goodStack;
    }

    renderGoodStackInCart() {
        return `<div class="cart-data">${this.goodStackInCart.good.title}</div>
        <div class="cart-data">${this.goodStackInCart.good.price}$</div>
        <div class="cart-data">${this.goodStackInCart.count}</div>
        <div class="cart-data">${this.goodStackInCart.getStackPrice()}$</div>`
    }


}

class CartRender {
    constructor(cart) {
        this.goods = cart;
    }

    renderCart() {
        let cartHeaderHTML = '<div class="cart-wrapper"><div \
        class="cart-header">Name</div><div class="cart-header">Price</div>\
        <div class="cart-header">Qty</div><div class="cart-header">Subtotal\
        </div>'
        if (this.goods.list.length) {
            let stacksList = this.goods.list
                .map(stack => new GoodInCartRenderer(stack))
            let cartHTML = stacksList.map(stack => stack.renderGoodStackInCart())
                .join('') + '</div>';
            let totalQty = this.goods.list.map(stack => stack.getCount())
                .reduce((a, b) => a + b);
            let totalPrice = this.goods.list.map(stack => stack.getStackPrice())
                .reduce((a, b) => a + b);
            let totalString = `<div class="cart-total">${totalQty} pieces of goods\
         for ${totalPrice}$</div>`;
            document.querySelector('.cart').innerHTML = cartHeaderHTML +
                cartHTML + totalString
        } else {
            document.querySelector('.cart').innerHTML = cartHeaderHTML
        }
    }
}

const cart = new Cart();
const showcase = new Showcase(cart);
showcase.fetchGoods();
cart.fetchCart();
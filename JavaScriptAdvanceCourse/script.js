'use strict'
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
    }

    add(good) {
        const idx = this.list.findIndex((stack) => stack.getGoodId() == good.id)

        if (idx >= 0) {
            this.list[idx].add()
        } else {
            this.list.push(new GoodStack(good))
        }

    }

    remove(id) {
        const idx = this.list.findIndex((stack) => stack.getGoodId() == id)

        if (idx >= 0) {
            this.list[idx].remove()

            if (this.list[idx].getCount() <= 0) {
                this.list.splice(idx, 1)
            }
        }

    }
}

class Showcase {
    constructor(cart) {
        this.list = [];
        this.cart = cart;
    }

    fetchGoods() {
        this.list = [
            new Good({ id: 1, title: 'Shirt', price: 150 }),
            new Good({ id: 2, title: 'Socs', price: 50 }),
            new Good({ id: 3, title: 'Jacket', price: 350 }),
            new Good({ id: 4, title: 'Shoes', price: 250 }),
        ]
    }

    addToCart(id) {
        const idx = this.list.findIndex((good) => id == good.id)

        if (idx >= 0) {
            this.cart.add(this.list[idx])
        }
    }
}

class GoodRenderer {
    constructor(good) {
        this.good = good
    }

    renderGoodHTML() {
        return `<div class="goods-item"><div class="goods-item-image">
        </div><h3>${this.good.title}</h3><p>${this.good.price}$</p></div>`
    }
}

class ShowcaseRenderer {
    constructor(showcase) {
        this.showcase = showcase;
    }

    renderShowcase() {
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
        let cartHeaderHTML = '<div class="cart-wrapper"><div class="cart-header">Name</div><div class="cart-header">Price</div><div class="cart-header">Qty</div><div class="cart-header">Subtotal</div>'
        let stacksList = this.goods.list.map(stack => new GoodInCartRenderer(stack))
        let cartHTML = stacksList.map(stack => stack.renderGoodStackInCart()).join('') + '</div>';
        let totalQty = this.goods.list.map(stack => stack.getCount())
            .reduce((a, b) => a + b);
        let totalPrice = this.goods.list.map(stack => stack.getStackPrice())
            .reduce((a, b) => a + b);
        let totalString = `<div class="cart-total">${totalQty} pieces of goods for ${totalPrice}$</div>`;
        document.querySelector('.cart').innerHTML = cartHeaderHTML + cartHTML + totalString;

    }
}

document.querySelector('.cart-button').addEventListener('click', event => {
    document.querySelector('.cart').classList.toggle('cart__active');
})


const cart = new Cart();
const showcase = new Showcase(cart);
showcase.fetchGoods();
const showcaseRenderer = new ShowcaseRenderer(showcase);
showcaseRenderer.renderShowcase();

showcase.addToCart(1);
showcase.addToCart(1);
showcase.addToCart(1);
showcase.addToCart(3);
showcase.addToCart(4);
showcase.addToCart(2);
showcase.addToCart(2);
showcase.addToCart(1);
showcase.addToCart(3);
showcase.addToCart(4);
cart.remove(2);

cart.remove(1);

const cartRenderer = new CartRender(cart);
cartRenderer.renderCart();

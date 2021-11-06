'use strict';
class CartList {
    productList = []
    /**
     * Function add product, qty of product, price of one product
     * and total price of products. In case of existed product function
     * recalculate total and qty of such product in cart
     * @param {string} name name of the product to add in cart
     * @param {float} price price of the product to add in cart
     * @returns undefiend
     */
    addToCart(name, price) {
        for (let product of this.productList) {
            if (product.name === name) {
                product.qty++;
                product.subTotal += price
                return;
            }
        }
        this.productList.push(
            {
                name: name,
                qty: 1,
                price: price,
                subTotal: price
            }
        )
    }
    /**
     * 
     * @returns {float} total price for all products in cart
     */
    getTotal() {
        let total = 0;
        this.productList.forEach(product => total += product.subTotal);
        return total;
    }
    /**
     * 
     * @returns {string} HTML blocks to insert cart list in page
     */
    render() {
        let cartHTML = ''
        this.productList.forEach(product => {
            cartHTML += `<div>${product.name}</div>
            <div>${product.qty} шт.</div>
            <div>$${product.price}</div>
            <div>$${product.subTotal}</div>`
        })
        return cartHTML
    }
}

const addTocharButton = document.querySelector('.featuredItems');
const openChartButton = document.querySelector('.cartIconWrap');
const chartList = document.querySelector('.cartList');

let basket = new CartList();

// event for click on add to cart button
addTocharButton.addEventListener('click', event => {
    if (event.target.localName != 'button' && event.target.parentNode.
        localName != 'button') {
        return
    }
    let itemEl = event.target
    //seek elements to get info about product from page
    while (!itemEl.classList.contains("featuredItem")) {
        itemEl = itemEl.parentNode
    }
    const itemDataPrice = Number.parseFloat(itemEl.
        querySelector(".featuredData>.featuredPrice").innerText.slice(1));
    const itemDataName = itemEl.querySelector(".featuredData>.featuredName").
        innerText;
    basket.addToCart(itemDataName, itemDataPrice);
    // when we add more products to cart we need to rerender cart list 
    //otherwise it's possible to have dublicates and incorrect remder.
    // Rerender should occur correctly even when cart list is open
    chartList.querySelectorAll('.cartWrapper>div:not(.cartHeader)').
        forEach(el => el.remove());
    // Insertion cart element on page
    chartList.querySelector('.cartWrapper').insertAdjacentHTML('beforeend',
        basket.render());
    // Insertion information about total price in cart list element
    document.querySelector('.cartTotalValue').innerText = basket.getTotal();
    // Insertion counter of objects in cart to span object on page
    let qtyProducts = Number.parseInt(document.
        querySelector('.cartIconWrap > span').innerText)
    if (!qtyProducts) {
        document.querySelector('.cartIconWrap > span').innerText = 1;
    } else {
        document.querySelector('.cartIconWrap > span').
            innerText = qtyProducts + 1;
    }

})

// to show cart list with products and prices
openChartButton.addEventListener('click', event => {
    chartList.classList.toggle('cartListActive');
}
);
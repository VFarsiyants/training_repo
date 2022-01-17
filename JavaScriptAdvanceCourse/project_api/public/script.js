const API_URL = "http://localhost:3000/api/v1/";

new Vue({
    el: "#app",
    data: {
        showcase: [],
        cart: [],
        isCartVisible: false
    },
    methods: {
        async postData(url = '', data = {}) {
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            });
            return await response;
        },

        onCartShow() {
            this.isCartVisible = !this.isCartVisible
        },

        addToBasket(id) {
            data = {
                id_product: id,
                quantity: 1
            };
            this.postData(`${API_URL}cart`, data).then(response => {
                if (response.status == 201) {
                    const idxGood = this.showcase.findIndex(good =>
                        good.id_product == id);
                    const good = this.showcase[idxGood]
                    const idxCart = this.cart.findIndex(stack =>
                        stack.id_product == id);
                    if (idxCart >= 0) {
                        ++this.cart[idxCart].quantity;
                        this.cart[idxCart].price += good.price;
                    } else {
                        this.cart.push({
                            id_product: data.id_product,
                            price: good.price,
                            product_name: good.product_name,
                            quantity: 1
                        })
                    }
                }
            });
        },

        removeFromBasket(id) {
            this.postData(`${API_URL}cart/remove`,
                { id_product: id }).then(
                    response => {
                        if (response.status == 201) {
                            const idxGood = this.showcase.findIndex(good =>
                                good.id_product == id);
                            const idxStack = this.cart.findIndex(stack =>
                                stack.id_product == id);
                            if (this.cart[idxStack].quantity == 1) {
                                this.cart.splice(idxStack, 1)
                            } else {
                                --this.cart[idxStack].quantity;
                                this.cart[idxStack].price -= this
                                    .showcase[idxGood].price
                            }
                        };
                    }
                )
        }
    },

    mounted() {
        fetch(`${API_URL}showcase`).then(res => res.json()).
            then(data => {
                this.showcase = data
            })

        fetch(`${API_URL}cart`).then(res => res.json())
            .then(data => { this.cart = data; })
    },
})

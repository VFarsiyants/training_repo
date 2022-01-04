const API_URL = "http://localhost:3000/api/v1/";

new Vue({
    el: "#app",
    data: {
        showcase: [],
        cart: [],
        isCartVisible: false
    },
    methods: {
        onCartShow() {
            this.isCartVisible = !this.isCartVisible
        }
    },
    mounted() {
        fetch(`${API_URL}showcase`).then(res => res.json()).
            then(data => {
                this.showcase = data
            })

        fetch(`${API_URL}cart`).then(res => res.json())
            .then(data => { this.cart = data; })
    }
})

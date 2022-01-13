Vue.component('cart',
    {
        template: `
        <div class="cart">
            <div class="cart-headers">
            <div class="cart-header">Name</div>
            <div class="cart-header">Qty</div>
            <div class="cart-header">Subtotal</div>
            <div class="cart-header">Remove</div>'
            </div class="cart-headers">
            <cartgood v-for="item of list" :goodStackInCart="item" \
            v-on:remove="removeFromCart($event)"></cartgood>
        </div>
        `,
        props: ['list'],
        methods: {
            removeFromCart(id) {
                this.$emit('update:cart:remove', id);
            }
        }
    }
)
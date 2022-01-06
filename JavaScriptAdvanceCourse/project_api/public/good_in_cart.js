Vue.component('cartgood',
    {
        template: `
        <div class="cart_line">
            <div class="cart-data">{{ goodStackInCart.product_name }}</div>
            <div class="cart-data">{{ goodStackInCart.quantity }}</div>
            <div class="cart-data">{{ goodStackInCart.price }}$</div>
            <button class="cart-data" \
            :data-product_id="goodStackInCart.id_product" type="button" \
            v-on:click="removeGood">Remove from Cart</button>
        </div>
        `,
        props: ['goodStackInCart'],
        methods: {
            removeGood(event) {
                const id = event.target.dataset.product_id;
                this.$emit('remove', id)
            }
        }
    }
)
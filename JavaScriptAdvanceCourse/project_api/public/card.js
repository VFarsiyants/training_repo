Vue.component('card',
    {
        template: `
        <div class="goods-item">
            <div class="goods-item-image"></div>
            <h3>{{ good.product_name }}</h3>
            <p>{{ good.price }}$</p>
            <button class="add-button" :data-product_id="good.id_product" \
            type="button">Add to Cart</button>
        </div>
        `,
        props: ['good']
    }
)
<template>
  <div class="goods-item">
    <div class="goods-item-image"></div>
    <h3>{{ good.product_name }}</h3>
    <p>{{ good.price }}$</p>
    <button
      class="add-button"
      :data-product_id="good.id_product"
      type="button"
      v-on:click="buy"
    >
      Add to Cart
    </button>
  </div>
</template>

<script>
export default {
  name: "card",
  props: ["good"],
  methods: {
    buy(event) {
      this.$emit("add", event.target.dataset.product_id);
    },
  },
};
</script>

<style scoped>
.goods-item {
  padding-top: 10px;
  align-items: center;
  display: flex;
  flex-direction: column;
  width: 300px;
  border: solid black 1px;
  margin: 10px;
}

.goods-item-image {
  width: 200px;
  height: 200px;
  border: solid black 1px;
}

.add-button {
  margin: 10px;
  padding: 0px 10px;
}
</style>
<template>
  <div class="cart">
    <div class="cart-headers">
      <div class="cart-header">Name</div>
      <div class="cart-header">Qty</div>
      <div class="cart-header">Subtotal</div>
      <div class="cart-header">Remove</div>
    </div>
    <cartgood
      v-for="item of list"
      v-bind:key="item.id_product"
      :goodStackInCart="item"
      v-on:remove="removeFromCart($event)"
    ></cartgood>
  </div>
</template>

<script>
import cartgood from "./Cartgood.vue";
export default {
  name: "cart",
  components: {
    cartgood,
  },
  props: ["list"],
  methods: {
    removeFromCart(id) {
      this.$emit("update:cart:remove", id);
    },
  },
};
</script>

<style scoped>
.cart {
  position: absolute;
  width: 700px;
  display: flex;
  flex-direction: column;
  right: 140px;
  top: 20px;
  background-color: lightgreen;
}

.cart-headers {
  display: flex;
}

.cart-header {
  padding-bottom: 10px;
  border-bottom: 3px solid black;
  border-right: 1px solid grey;
  padding-top: 5px;
  padding-left: 5px;
  width: 200px;
  text-align: center;
}
</style>
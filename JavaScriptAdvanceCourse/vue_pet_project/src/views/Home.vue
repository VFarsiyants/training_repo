<template>
  <div v-if="isServerAvailable">
    <header>
      <div class="cart-info">
        <button v-on:click="onCartShow" class="cart-button" type="button">
          Cart
        </button>
        <cart
          v-if="isCartVisible"
          :list="cart"
          v-on:update:cart:remove="removeFromBasket($event)"
        ></cart>
      </div>
    </header>
    <main>
      <showcase
        :list="showcase"
        v-on:update:cart:add="addToBasket($event)"
      ></showcase>
    </main>
  </div>
  <div v-else>
    <error></error>
  </div>
</template>

<script>
const API_URL = "http://localhost:3000/api/v1/";

import cart from "../components/Cart.vue";
import showcase from "../components/Showcase.vue";
import error from "../components/Error.vue";

export default {
  name: "Home",
  components: {
    cart,
    showcase,
    error,
  },
  data() {
    return {
      showcase: [],
      cart: [],
      isCartVisible: false,
      isServerAvailable: true,
    };
  },
  methods: {
    async postData(url = "", data = {}) {
      const response = await fetch(url, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });
      return await response;
    },

    onCartShow() {
      this.isCartVisible = !this.isCartVisible;
    },

    addToBasket(id) {
      const data = {
        id_product: id,
        quantity: 1,
      };
      this.postData(`${API_URL}cart`, data).then((response) => {
        if (response.status == 201) {
          const idxGood = this.showcase.findIndex(
            (good) => good.id_product == id
          );
          const good = this.showcase[idxGood];
          const idxCart = this.cart.findIndex(
            (stack) => stack.id_product == id
          );
          if (idxCart >= 0) {
            ++this.cart[idxCart].quantity;
            this.cart[idxCart].price += good.price;
          } else {
            this.cart.push({
              id_product: data.id_product,
              price: good.price,
              product_name: good.product_name,
              quantity: 1,
            });
          }
        }
      });
    },

    removeFromBasket(id) {
      this.postData(`${API_URL}cart/remove`, { id_product: id }).then(
        (response) => {
          if (response.status == 201) {
            const idxGood = this.showcase.findIndex(
              (good) => good.id_product == id
            );
            const idxStack = this.cart.findIndex(
              (stack) => stack.id_product == id
            );
            if (this.cart[idxStack].quantity == 1) {
              this.cart.splice(idxStack, 1);
            } else {
              --this.cart[idxStack].quantity;
              this.cart[idxStack].price -= this.showcase[idxGood].price;
            }
          }
        }
      );
    },
  },

  mounted() {
    fetch(`${API_URL}showcase`)
      .then((res) => res.json())
      .then((data) => {
        this.showcase = data;
      })
      .catch((err) => (this.isServerAvailable = false));

    fetch(`${API_URL}cart`)
      .then((res) => res.json())
      .then((data) => {
        this.cart = data;
      })
      .catch((err) => (this.isServerAvailable = false));
  },
};
</script>

<style scoped>
header {
  display: flex;
  height: 75px;
  background-color: rgba(89, 206, 167, 0.438);
  border: solid black 1px;
  justify-content: flex-end;
  margin-bottom: 30px;
}

header button {
  height: 30px;
  width: 150px;
  border-radius: 10px;
}
main {
  max-width: 1400px;
  margin: 0 auto;
}
.cart-info {
  align-self: center;
  position: relative;
  margin-right: 50px;
}
</style>

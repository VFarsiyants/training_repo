<template>
  <div class="goods-list">
    <card
      v-for="item of list"
      v-bind:key="item.id_product"
      :good="item"
      v-on:add="addGood($event)"
    ></card>
  </div>
</template>

<script>
import card from "./Card.vue";
export default {
  name: "showcase",
  components: {
    card,
  },
  props: ["list"],
  methods: {
    addGood(id) {
      this.$emit("update:cart:add", id);
    },
  },
};
</script>

<style scoped>
.goods-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
}
</style>
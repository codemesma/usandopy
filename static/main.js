var app = new Vue({
  el: "#app",
  data: {
    product: "Socks",
    image: "./img/cute.jpg",
    inStock: true,
    details: ["80 of goodness", "20 of badness", "Gender-cute"],
    variants: [
      { id: 1, color: "Cute", image: "./img/cute.jpg" },
      { id: 2, color: "Eat", image: "./img/eat.jpg" },
    ],
    cart: 0,
  },
  methods: {
    addToCart: function () {
      this.cart += 1;
    },
    updateProduct: function (i) {
      this.image = i;
    },
  },
});

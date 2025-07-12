<template>
    <div class="hello">
        <Title>PaperWaves</Title>
        <p>Formula</p>
        <textarea v-model="formula" cols="30" rows="10"></textarea>
        <p>Result</p>
        <vue-mathjax :formula="formula"></vue-mathjax>
    </div>
</template>

<script>
import { VueMathjax } from "vue-mathjax";
export default {
    components: {
        "vue-mathjax": VueMathjax,
    },
    name: "HelloWorld",
    data() {
        return {
            formula: "$$x = {-b \\pm \\sqrt{b^2-4ac} \\over 2a}.$$",
            msg: "Welcome to Your Vue.js App",
        };
    },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
    font-weight: normal;
}
ul {
    list-style-type: none;
    padding: 0;
}
li {
    display: inline-block;
    margin: 0 10px;
}
a {
    color: #42b983;
}
</style>

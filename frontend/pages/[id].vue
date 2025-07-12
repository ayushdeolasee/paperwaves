<template>
    <div class="container">
        <Title>PaperWaves</Title>
        <h1 class="title">
            {{ title }}
        </h1>
        <p><span class="keyWords">Authors:</span> {{ author }}</p>
        <p><span class="keyWords">Subject:</span> {{ subject }}</p>
        <p><span class="keyWords">Published:</span> {{ date }}</p>
        <!-- <vue-mathjax :formula="text" class="description"> -->
        <p class="description">{{ summary }}</p>
        <!-- </vue-mathjax> -->
        <NuxtLink :to="pdfURL"
            ><button class="button">Read Now</button>
        </NuxtLink>
    </div>
</template>

<script setup>
import { VueMathjax } from "vue-mathjax";
const text = "hello world";
const { id } = useRoute().params;
const url = "http://localhost:8000/info/";
const newUrl = url.concat(id);
let pdfURL = "";
console.log(newUrl);
let title = "";
let author = "";
let summary = "";
let subject = "";
var datetime = new Date();
var date;

await fetch(newUrl)
    .then((response) => {
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
    })
    .then((data) => {
        // console.log(data["Title"]);
        title = data["Title"];
        const authorArray = data["Authors"];
        author = authorArray.join(", ");
        console.log(author);
        summary = data["Summary"];
        date = datetime.toDateString();
        date = date.replace(" ", ", ");
        subject = data["Primary_category"];
        pdfURL = data["PDF_URL"];
    })
    .catch((error) => {
        console.error("Error", error);
    });
console.log("Title: ", title);
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@300&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@200&display=swap");
.button {
    outline: none;
    border: none;
    background: #20b2ab;
    color: white;
    width: 20rem;
    height: 5rem;
    border-radius: 17px;
    font-size: 19px;
    margin-top: 7rem;
}
.button:hover {
    cursor: pointer;
}
.container {
    text-align: center;
    padding: 10px;
}
.keyWords {
    color: #006993;
}
p {
    font-family: "Poppins";
    font-weight: 250;
    padding-left: 10px;
    padding-right: 10px;
}
.title {
    font-family: "Poppins";
    text-align: center;
    font-size: 30px;
    font-weight: 800;
}
.description {
    margin-top: 3rem;
}
</style>

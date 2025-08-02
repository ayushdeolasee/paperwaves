
<template>
    <div class="container">
        <div class="backButton" @click="goBack">
            <img src="/back.svg" alt="Back" />
        </div>
        <h1 class="title">{{ title }}</h1>
        <p class="meta"><span class="keyWords">Authors:</span> {{ author }}</p>
        <p class="meta"><span class="keyWords">Subject:</span> {{ subject }}</p>
        <p class="meta"><span class="keyWords">Published:</span> {{ published }}</p>
        <p class="summary"><span class="keyWords">Summary:</span> {{ summary }}</p>
    </div>
</template>

<script setup>
import { useRoute } from 'vue-router';

const route = useRoute();
const id = route.params.id;

let title = "";
let author = "";
let published = "";
let subject = "";
let summary = "";

const { data: information, error } = await useFetch(`http://127.0.0.1:8000/${id}`);

if (error.value) {
    console.error("Error fetching data:", error.value);
}

if (information.value) {
    const info = information.value;
    title = info.Title;
    author = info.Authors.join(', ');
    published = new Date(info.Published).toDateString();
    subject = info.Primary_category;
    summary = info.Summary;
}

const goBack = () => {
    window.history.back();
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@500&display=swap");

.container {
    font-family: "Poppins", sans-serif;
    padding: 40px;
    width: 100%;
    box-sizing: border-box;
}

.title {
    font-size: 36px;
    margin-bottom: 20px;
}

.meta {
    font-size: 18px;
    margin-bottom: 10px;
}

.keyWords {
    color: #006993;
    font-weight: 600;
}

.summary {
    font-size: 16px;
    line-height: 1.7;
    margin-top: 30px;
}

.backButton {
    position: fixed;
    top: 20px;
    left: 20px;
    cursor: pointer;
    background-color: #f1f1f1;
    border-radius: 50%;
    padding: 10px;
    display: flex;
    justify-content: center;
    align-items: center;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    z-index: 1000;
}

.backButton img {
    width: 24px;
    height: 24px;
}
</style>

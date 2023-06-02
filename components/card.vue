<template>
    <div class="card">
        <h1 class="cardTitle">
            {{ title }}
        </h1>
        <p>
            <span class="keyWords">Authors:</span>
            {{ author }}
        </p>
        <p><span class="keyWords">Subject: </span>{{ subject }}</p>
        <p><span class="keyWords">Published:</span> {{ published }}</p>
    </div>
</template>

<script setup>
// const { title, author, published, subject } = defineProps([
//     "title",
//     "author",
//     "published",
//     "subject",
// ]);
const { information } = defineProps(["information"]);
let title = "";
let author = "";
let published = "";
let subject = "";
var datetime = new Date();
var date;
// const id = "";

// id = information["Entry_id"];
// console.log(information["Authors"][0]);

title = information["Title"];
// author = information["Authors"];
const authorArray = information["Authors"];
author = authorArray.join(", ");
// createAuthorString();
published = information["Published"];
subject = information["Primary_category"];
datetime = new Date(published);
date = datetime.toDateString();
date = date.replace(" ", ", ");
</script>

<style scoped>
.cardTitle {
    line-height: 40px;
    font-size: 25px;
}
.card {
    background-color: #defdfb;
    width: 100%;
    /* padding-left: 20px; */
    /* padding-right: 20px; */
    /* padding-top: 2px; */
    padding: 20px;
    padding-top: 5px;
    border-radius: 17px;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
}
.keyWords {
    color: #006993;
}
</style>

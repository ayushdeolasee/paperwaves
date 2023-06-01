<template>
    <div class="parent">
        <div class="searchBar">
            <img class="icon" src="/find.svg" />
            <input class="input" v-model="message" placeholder="Search" />
        </div>
        <div v-for="i in finalData" class="cards">
            <!-- <card
                :title="title"
                :author="author"
                :published="date"
                :subject="subject"
            /> -->
            <card :information="finalData[i]" />
        </div>
    </div>
</template>

<script setup>
let title = "";
let summary = "";
let author = "";
let published = "";
let subject = "";
var datetime = new Date();
var date;
let finalData;

await fetch("http://127.0.0.1:8000")
    .then((response) => {
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
    })
    .then((data) => {
        finalData = data;
        while (True) {
            if (i == lenght(data)) {
                break;
            }
        }
        console.log(data);
        title = data["Title"];
        summary = data["Summary"];
        author = data["Authors"];
        published = data["Published"];
        subject = data["Primary_category"];
        // console.log(published);
        datetime = new Date(published);
        date = datetime.toDateString();
        date = date.replace(" ", ", ");
        // console.log(title);
        // console.log(finalData);
    })
    .catch((error) => {
        console.error("Error:", error);
    });
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@500&display=swap");
.cardTitle {
    line-height: 40px;
    font-size: 25px;
}
.card1 {
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
.cards {
    margin-top: 4rem;
    display: flex;
    justify-content: center;
    width: 79%;
    font-family: "Poppins";
}
.keyWords {
    color: #006993;
}
.input {
    /* width: 108rem; */
    width: 90%;
    margin-left: 0.7rem;
    font-size: 24px;
    border: none;
    outline: none;
    background-color: transparent;
    /* position: relative;
    top: 25%;
    transform: translate(0, -50%); */
}
.parent {
    /* position: absolute;
    top: 5%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 100%; */
    /* margin: auto; */
    display: flex;
    justify-content: space-around;
    flex-direction: column;
    align-items: center;
    margin-top: 1.4rem;
}
.icon {
    margin-left: 0.7rem;
    height: 2.2rem;
    vertical-align: center;
}
.searchBar {
    background-color: #f1f1f1;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    height: 3rem;
    width: 80%;
    border-radius: 17px;
    display: flex;
    align-items: center;
}
</style>

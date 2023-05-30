<template>
    <div class="card">
        <h1 class="cardTitle">
            {{ information.title }}
        </h1>
        <p>
            <span class="keyWords">Authors:</span>
            {{ information.author }}
        </p>
        <p><span class="keyWords">Subject: </span>{{ information.subject }}</p>
        <p><span class="keyWords">Published:</span> {{ information.date }}</p>
    </div>
</template>

<script setup>
const { information } = defineProps(["information"]);
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

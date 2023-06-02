<template>
    <div class="container">
        <h1 class="title">
            {{ title }}
        </h1>
        <p>
            <span class="keyWords">Authors:</span> Ingeborg G. Gjerde, Ridgway
            Scott
        </p>
        <p><span class="keyWords">Subject:</span> Fluid Dynamics</p>
        <p><span class="keyWords">Published:</span> 30th December 2022</p>
        <p class="description">
            Stokes flow equations, used to model creeping flow, are a commonly
            used simplification of the Navier--Stokes equations. The
            simplification is valid for flows where the inertial forces are
            negligible compared to the viscous forces. In infinite domains, this
            simplification leads to a fundamental paradox. In this work we
            review the Stokes paradox and present new insights related to recent
            research. We approach the paradox from three different points of
            view: modern functional analysis, numerical simulations, and
            classical analytic techniques. The first approach yields a novel,
            rigorous derivation of the paradox. We also show that relaxing the
            Stokes no-slip condition (by introducing a Navier's friction
            condition) in one case resolves the Stokes paradox but gives rise to
            d'Alembert's paradox. The Stokes paradox has previously been
            resolved by Oseen, who showed that it is caused by a limited
            validity of Stokes' approximation. We show that the paradox still
            holds for the Reynolds--Orr equations describing kinetic energy flow
            instability, meaning that flow instability steadily increases with
            domain size. We refer to this as an instability paradox.
        </p>
        <NuxtLink><button class="button">Read Now</button> </NuxtLink>
    </div>
</template>

<script setup>
const { id } = useRoute().params;
const url = "http://localhost:8000/info/";
const newUrl = url.concat(id);
console.log(newUrl);
const title = "";

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

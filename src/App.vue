<template>
  <router-view/>
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins&family=Zilla+Slab:wght@500&display=swap');

body {
  padding: 0;
  margin: 0;
  height: 100vh;
  width: 100vw;
  font-family: 'Poppins', sans-serif;
  font-size: 12pt;
}

h1, h2, h3, h4 {
  font-family: 'Zilla Slab', serif;
}

h1 {
  font-size: 3rem;
}

h2 {
  font-size: 2rem;
}

#app {
  padding: 0;
  margin: 0;
  height: 100%;
}

#app > div {
  height: 100%;
}
</style>

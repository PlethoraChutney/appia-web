<template>
  <router-view/>
</template>

<script>
import {store} from './store.js'

export function sendRequest(body, dest = '/api') {
    return fetch(dest, {
        method: 'POST',
        mode: 'cors',
        cache: 'no-cache',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json'
        },
        redirect: 'follow',
        referrerPolicy: 'no-referrer',
        body: JSON.stringify(body)
    })
}

export default {
  data() {
    return {
      store
    }
  },
  created() {
      // hacky way to wait until router has finished reading
      // everything in
      window.setTimeout(() => {
          this.store.setExpList(this.$route.params.experiment.split('+'));
          this.store.expListLoaded = true;
      }, 200)
  },
  watch: {
    'store.currentExperimentList'(newValue) {
      if (newValue.join('+') !== this.$route.params.experiment && this.store.expListLoaded) {
        this.$router.push({
          name: 'traces',
          params: {
            experiment: newValue.join('+')
          }
        })
      }
    },
    '$route.params.experiment'(newValue = '') {
      if (newValue !== this.store.currentExperimentList) {
        this.store.setExpList(newValue.split('+'))
      }
    }
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins&family=Zilla+Slab:wght@500&display=swap');

body {
  padding: 0;
  margin: 0;
  height: 100vh;
  width: 100vw;
  font-family: 'Poppins', sans-serif;
  font-size: 12pt;
  background-color: #FFEE8F;
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

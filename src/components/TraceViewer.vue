<template>
    <div id="trace-viewer">
        <h1 id="appia-title">Appia</h1>
        <TracePicker/>
    </div>
</template>

<script>
import TracePicker from '@/components/TracePicker.vue'
import {store} from '@/store.js'

export default {
    data() {
        return {
            store
        }
    },
    components: {
        TracePicker
    }
}
</script>

<style scoped>
#trace-viewer {
    display: grid;
    height: 100%;
    grid-template-rows: min-content auto;
    grid-template-columns: 1fr 1fr 1fr;
    grid-template-areas: 
        "header header header"
        "sidebar main main"
    ;
}

#appia-title {
    grid-area: header;
    margin: auto;
}
</style>
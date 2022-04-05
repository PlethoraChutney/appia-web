<template>
    <div id="trace-viewer">
        <div id="appia-title">
            <h1>Appia</h1>
            <h2
            v-if="store.currentExperimentList.length !== 0 && store.currentExperimentList[0] !== ''"
            >Currently viewing {{store.currentExperimentList.join(', ')}}</h2>
            <h2 v-else>Pick an experiment below to start</h2>
        </div>
        <SidebarPanel/>
    </div>
</template>

<script>
import SidebarPanel from '@/components/SidebarPanel.vue'
import {store} from '@/store.js'

export default {
    data() {
        return {
            store
        }
    },
    components: {
        SidebarPanel
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

#appia-title > h1, #appia-title > h2 {
    margin: 0;
    text-align: center;
}

</style>
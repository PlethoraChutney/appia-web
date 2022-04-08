<template>
    <div id="trace-viewer">
        <div id="appia-title">
            <h1>Appia</h1>
            <p
            v-if="store.currentExperimentList.length !== 0 && store.currentExperimentList[0] !== ''"
            >Currently viewing {{store.currentExperimentList.join(', ')}}</p>
            <p v-else>Pick an experiment below to start</p>
        </div>
        <SidebarPanel/>
        <PlotPanel/>
    </div>
</template>

<script>
import SidebarPanel from '@/components/SidebarPanel.vue'
import PlotPanel from '@/components/PlotPanel.vue'
import {store} from '@/store.js'

export default {
    data() {
        return {
            store
        }
    },
    components: {
        SidebarPanel,
        PlotPanel
    }
}
</script>

<style scoped>
#trace-viewer {
    display: grid;
    height: 100%;
    width: 90%;
    max-width: 1400px;
    margin: auto;
    grid-template-rows: min-content auto;
    grid-template-columns: 1fr 1fr 1fr;
    grid-template-areas: 
        "header header header"
        "sidebar main main"
    ;
    gap: 1em;
    background-color: #FFFEFA;
    border-radius: 10px;
    border: 6px solid #F7E372;
    padding: 20px;
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
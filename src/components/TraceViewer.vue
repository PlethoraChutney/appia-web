<template>
    <div id="trace-viewer">
        <div id="appia-title">
            <h1>Appia</h1>
            <h2
            v-if="$route.params.experiment"
            >Currently viewing {{experimentList}}</h2>
        </div>
        <SidebarPanel/>
    </div>
</template>

<script>
import SidebarPanel from '@/components/SidebarPanel.vue'

export default {
    components: {
        SidebarPanel
    },
    computed: {
        experimentList() {
            return this.$route.params.experiment.replaceAll('+', ', ');
        }
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
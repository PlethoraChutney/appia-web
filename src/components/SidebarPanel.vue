<template>
    <div id="sidebar-panel">
        <TracePicker/>
    </div>
</template>

<script>
import TracePicker from './TracePicker.vue'
export default {
    components: {
        TracePicker
    }
}
</script>

<style scoped>
    div#sidebar-panel {
        grid-area: sidebar;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        align-items: center;
    }
</style>
<template>
    <div id="trace-picker">
        <Multiselect
        id="trace-multiselect"
        v-model="this.store.currentExperimentList"
        :options="options"
        :mode="`multiple`"
        :searchable="true"
        :hideSelected="false"
        :closeOnSelect="false"
        :placeholder="`Pick an experiment`"
        />
    </div>
</template>

<script>
import Multiselect from '@vueform/multiselect'
import {store} from '@/store.js'

export default {
    components: {
        Multiselect
    },
    data() {
        return {
            store,
            experimentsSelected: null,
            options: [
                'test1',
                'test2',
                'test3'
            ]
        }
    }
}
</script>

<style src="@vueform/multiselect/themes/default.css"></style>
<style scoped>
    #trace-picker {
        width: 90%;
    }

    #trace-multiselect > input {
        position: unset;
    }
</style>
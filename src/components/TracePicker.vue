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
import {sendRequest} from '@/App.vue'

export default {
    components: {
        Multiselect
    },
    data() {
        return {
            store,
            experimentsSelected: null,
            options: []
        }
    },
    mounted() {
        sendRequest({'action': 'get_experiment_list'})
        .then(request => request.json()).then(data => {
            this.options = data
        })
    }
}
</script>

<style src="@vueform/multiselect/themes/default.css"></style>
<style scoped>
    #trace-picker {
        width: 90%;
        --ms-option-bg-pointed: #FFEE8F;
        --ms-option-bg-selected: #7D72F7;
        --ms-option-bg-selected-pointed: #372CAB;
    }

    #trace-multiselect > input {
        position: unset;
    }
</style>
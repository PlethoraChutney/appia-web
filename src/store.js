import {reactive} from 'vue'

export const store = reactive({
    currentExperimentList: [],
    expListLoaded: false,
    setExpList(experimentList) {
        this.currentExperimentList = experimentList;
    },
    currentDataJSON: null
})
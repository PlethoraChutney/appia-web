import {reactive} from 'vue'

export const store = reactive({
    currentExperimentList: [],
    expListLoaded: false,
    setExpList(experimentList) {
        this.currentExperimentList = experimentList;
    },
    hplcSamples: null,
    hplcDataRaw: null,
    hplcDataNorm: null,
    fplcData: null
})
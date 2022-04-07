<template>
    <div id="plot-panel">
        <div id="raw-plot">
            <h2>Signal</h2>
            <div id="hplc-raw-plot">
            </div>
        </div>
    </div>
</template>

<script>
import {store} from '@/store.js'
import {toJSON} from "danfojs"

export default {
    data() {
        return {
            store
        }
    },
    computed: {
        hplcSignalDF() {
            if (this.store.hplcDataFrame) {
                return this.store.hplcDataFrame.query({
                    "column": "Normalization",
                    "is": "==",
                    "to": "Signal"
                })
            } else {
                return null
            }
        }
    },
    watch: {
        hplcSignalDF() {
            let data = toJSON(this.hplcSignalDF)
            console.log(data)
        }
    }
}
</script>

<style scoped>
#plot-panel {
    grid-area: main;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
}
</style>
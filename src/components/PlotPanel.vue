<template>
    <div id="plot-panel">
        <div class="plot">
            <h2>Signal</h2>
            <div id="hplc-raw-plot" class="plot">
            </div>
        </div>
    </div>
</template>

<script>
import {store} from '@/store.js'
import Plotly from 'plotly.js-dist'

export default {
    data() {
        return {
            store
        }
    },
    watch: {
        'store.hplcDataRaw'() {
            let hplcData = [];
            this.store.hplcSamples.forEach(e => {
                hplcData.push({
                    type: 'scatter',
                    mode: 'lines',
                    x: store.hplcDataRaw.mL,
                    y: store.hplcDataRaw[e]
                })
            })

            let layout = [];

            let config = {responsive: true};
            Plotly.newPlot(
                'hplc-raw-plot',
                hplcData,
                layout,
                config
            )
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

.plot {
    width: 100%;
}
</style>
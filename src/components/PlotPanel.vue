<template>
    <div id="plot-panel">
        <div id="raw-plot-container" class="plot">
            <h2>Signal</h2>
            <div id="hplc-raw-plot" class="plot">
            </div>
        </div>
    </div>
</template>

<script>
import {store} from '@/store.js'
import * as Plot from "@observablehq/plot";

export default {
    data() {
        return {
            store
        }
    },
    mounted() {
        let newPlot = Plot.plot({
                    marks: [
                        Plot.line({'test': [1, 2, 3], 'ytest': [2, 3, 4], 'color': ['red', 'red', 'red']},
                        {x: 'test', y: 'ytest', stroke: 'color'}
                    )]
                });

        document.getElementById('hplc-raw-plot').appendChild(newPlot);
    },
    watch: {
        'store.hplcDataRaw'() {
            let newPlot = Plot.plot({
                marks: [
                    Plot.line(store.hplcDataRaw, {
                        x: 'mL',
                        y: 'Signal',
                        stroke: 'Sample'
                    })
                ]
            })

            let plotContainer = document.getElementById('raw-plot-container');
            plotContainer.removeChild(plotContainer.lastChild);
            plotContainer.appendChild(newPlot);
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
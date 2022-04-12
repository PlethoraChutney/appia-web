<template>
    <div id="plot-panel">
        <div id="raw-plot-container" class="plot">
            <h2 class="plot-header">Signal</h2>
            <div id="hplc-raw-plot" class="plot">
            </div>
        </div>
    </div>
</template>

<script>
import {store} from '@/store.js'
import Plotly from 'plotly.js-dist-min'

export default {
    data() {
        return {
            store
        }
    },
    watch: {
        'store.hplcDataRaw'() {

            let data = []
            for (let i = 0; i < this.store.hplcDataRaw.channels.length; i++) {
                let channel = this.store.hplcDataRaw.channels[i];
                this.store.hplcDataRaw[channel].samples.forEach(sample => {
                    let trace = {
                        x: this.store.hplcDataRaw[channel].data.Time,
                        y: this.store.hplcDataRaw[channel].data[sample],
                        name: sample,
                        type: 'scatter'
                    };
                    if (i > 0) {
                        trace['xaxis'] = `x${i+1}`;
                        trace['yaxis'] = `y${i+1}`;
                    }
                    data.push(trace);
                })
            }

            let layout = {
                grid: {
                    rows: 2,
                    columns: 1,
                    pattern: 'independent'
                }
            };

            let config = {
                displaylogo: false,
                responsive: true
            }

            Plotly.newPlot('hplc-raw-plot', data, layout, config);
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

.plot-header {
    text-align: center;
}
</style>
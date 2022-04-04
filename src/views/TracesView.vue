<template>
  <div class="home">
    <TraceViewer/>
  </div>
</template>

<script>
// @ is an alias to /src
import TraceViewer from '@/components/TraceViewer.vue'

export default {
  name: 'TracesView',
  components: {
    TraceViewer
  }
}
</script>

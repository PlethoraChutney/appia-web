<template>
  <div class="home" style="width: 100%;">
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

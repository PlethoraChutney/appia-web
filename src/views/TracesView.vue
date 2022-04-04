<template>
  <div class="home">
    <TraceViewer msg="Welcome to Your Vue.js App"/>
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

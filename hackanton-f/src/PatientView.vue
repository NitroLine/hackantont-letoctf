<template>
  <div>
     <h2 class="center">Ваше расписание </h2>
        {{error}}
        <el-card>
          <el-empty description="Пусто" v-if="tasks.length === 0"/>

      <el-timeline >
        <el-timeline-item
            v-for="(task, index) in tasks"
            :key="index"
            :icon="task.icon"
            :type="task.type"
            :color="task.color"
            :size="task.size"
            :hollow="task.hollow"
            :timestamp="task.time"
        >

            <h4>{{task.title}}</h4>
            <p>{{task.description}}</p>
            <p>{{task.doctor}}</p>
        </el-timeline-item>
      </el-timeline>
        </el-card>
  </div>

</template>

<script>
import { Check } from '@element-plus/icons-vue'

export default {
name: "PatientView",
  data(){
    return {
      tasks: [],
      error: null,
      token: null,
    }
  },
  beforeMount(){
    this.token = this.$route.query.token;
    if (this.token) {
      this.getTasks().catch((err) => this.error = String(err));
    }
  },
  methods:{
    async getTasks(){
      let resp = await fetch(`/tasks/${this.token}`,{
        headers: {
          'Accept': 'application/json'
        }
      });
      if (!resp.ok){
        throw Error(resp.statusText)
      }
      let result = await resp.json()
      // let result = [
      //   {name: 'Выпить таблетки', date: '12:22 12 сентября', description: "3 грамма для деда", done: true},
      //   {name: 'Выпить таблетки', date: '13:22 12 сентября ', description: "грамма для деда"}
      // ];
      this.tasks = result.map(this.prepeareTask)
    },

    prepeareTask(task){
      task.size = 'large';
      task.done = task.status;
      if (task.done){
        task.color = '#0bbd87';
        task.icon = Check;
      }
      return task;
    }
  }
}
</script>

<style scoped>

</style>
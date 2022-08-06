<template>
  <div>
    <el-empty v-if="tasks.length === 0" description="Пусто" />
    <div :key="task.date" v-for="task in tasks">
       <el-card  shadow="hover">
           <div style="padding: 14px">
             <h4> {{ task.name }}</h4>
          <span> {{ task.description }}</span>
           <el-button class="button" :type="task.type" :icon="task.icon" @click="changeTaskState(task)"></el-button>
          <div class="bottom">
            <time class="time">{{ task.date }}</time>
          </div>
        </div>
       </el-card>
    </div>
  </div>
</template>
<script setup>
import { Check } from '@element-plus/icons-vue'
</script>
<script>
export default {
  name: "TasksList",
  props: ["patient"],
  data(){
    return {
      tasks: []
    }
  },
  beforeMount(){
    this.getTasks().then((tasks) => this.tasks = tasks).catch((err) => this.error = String(err));
  },
  methods:{
    async getTasks(){
      let result = [
        {name: 'Выпить таблетки', date: '12:22 12 сентября', description: "3 грамма для деда", done: true},
        {name: 'Выпить таблетки', date: '13:22 12 сентября ', description: "грамма для деда"}
      ];
      return result.map(this.prepeareTask)
    },
    prepeareTask(task){``
      task.size = 'large';
      task.type = 'default'
      task.icon = null;
      if (task.done){
        task.type = 'success';
        task.icon = Check;
      }
      return task;
    },
    changeTaskState(task){
      task.done = !task.done
      // TODO: request here
      this.prepeareTask(task)
    }
  },
}
</script>

<style scoped>
.time {
  font-size: 12px;
  color: #999;
}

.bottom {
  margin-top: 13px;
  line-height: 12px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.button {
  padding: 0;
  min-height: auto;
  float:right;
  width: 50px;
  height: 50px;
}

.image {
  width: 100%;
  display: block;
}
</style>
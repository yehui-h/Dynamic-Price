<template>
  <div id="mainDiv">
    <el-main>
      <el-card class="box-card">
        <h1>Croissant</h1>
        <el-avatar
          :size="160"
          :src="require('../assets/Croissant.jpg')"
          @error="errorHandler"
        >
          <img :src="require('../assets/NoImage.png')" />
        </el-avatar>

        <div id="priceDiv">
          <h2>Price Now</h2>
          <p id="price">$7 !</p>
        </div>

        <h3>Stock</h3>
        <div class="demo-progress">
          <el-progress
            type="dashboard"
            :percentage="percentage"
            :color="colors"
          />
        </div>

        <bar-graph :width="auto" :height="'200px'"></bar-graph>
      </el-card>
    </el-main>
    <h5>{{ msg }}</h5>
  </div>
</template>

<script>
import BarGraph from "./BarGraph.vue";

export default {
  name: "MainContent",
  components: {
    BarGraph,
  },
  props: {
    msg: String,
  },

  data() {
    return {
      percentage: 15,
      colors: [
        { color: "#f56c6c", percentage: 20 },
        { color: "#e6a23c", percentage: 40 },
        { color: "#5cb87a", percentage: 60 },
        { color: "#1989fa", percentage: 80 },
        { color: "#6f7ad3", percentage: 100 },
      ],
    };
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#mainDiv {
  max-width: 500px;
  margin: auto;
}

#price {
  color: red;
  font-size: 40px;
  font-weight: bold;
  margin-top: 0px;
}

#echarts-box {
  width: 5px;
}

h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}

.demo-progress .el-progress--line {
  margin-bottom: 15px;
  width: 350px;
}
.demo-progress .el-progress--circle {
  margin-right: 15px;
}
</style>

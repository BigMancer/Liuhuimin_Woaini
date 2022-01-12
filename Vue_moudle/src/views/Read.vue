<template>
  <div class="Read">
    <v-md-preview :text="msg"></v-md-preview>
    <div id="send_button">
      <button @click="read_mail">
        <span>下一封信</span>
        <div class="liquid"></div>
      </button>
    </div>
  </div>
</template>

<script>
import { api_read_mail } from "@/apis/api";
import VMdPreview from "@kangc/v-md-editor/lib/preview";
import "@kangc/v-md-editor/lib/style/preview.css";
import githubTheme from "@kangc/v-md-editor/lib/theme/github.js";
import "@kangc/v-md-editor/lib/theme/style/github.css";
// highlightjs
import hljs from "highlight.js";

VMdPreview.use(githubTheme, {
  Hljs: hljs,
});
export default {
  name: "Read",
  components: {
    VMdPreview,
  },
  data() {
    return {
      msg: "",
      readed_list: [],
    };
  },
  methods: {
    async read_mail() {
      // 调用api接口，并传入参数
      const res = await api_read_mail({
        action: "read_mail",
        readed_list: this.readed_list,
      });
      // 获取的响应结果
      if (res.code == 0) {
        this.msg = res.msg;
        this.readed_list.push(res.mailID);
      }
    },
  },
  mounted() {
    this.read_mail();
  },
};
</script>

  <style scoped>
#container {
  display: inline;
}
#write {
  background-color: transparent;
  border: 0;
  outline: none;
  text-align: left;
  width: 100%;
  color: #000000;
  font-weight: bold;
  font-size: x-large;
}
button {
  position: relative;
  padding-top: 10px;
  padding-right: 112px;
  padding-left: 45px;
  padding-bottom: 8px;
  display: block;
  text-decoration: none;
  text-transform: uppercase;
  width: 86px;
  overflow: hidden;
  border-radius: 23px;
  border: none;
}

button span {
  position: relative;
  color: #fff;
  fot-size: 20px;
  font-family: Arial;
  letter-spacing: 8px;
  z-index: 1;
  white-space: nowrap;
}

button .liquid {
  position: absolute;
  top: -80px;
  left: 0;
  width: 176px;
  height: 200px;
  background: #f78da7;
  box-shadow: inset 0 0 50px rgba(0, 0, 0, 0);
  transition: 0.5s;
}

button .liquid::after,
button .liquid::before {
  content: "";
  width: 200%;
  height: 200%;
  position: absolute;
  top: 0;
  left: 50%;
  transform: translate(-50%, -75%);
  background: #fff;
}

button .liquid::before {
  border-radius: 45%;
  background: rgba(20, 20, 20, 1);
  animation: animate 5s linear infinite;
}

button .liquid::after {
  border-radius: 40%;
  background: rgba(20, 20, 20, 0.5);
  animation: animate 10s linear infinite;
}

button:hover .liquid {
  top: -120px;
}

@keyframes animate {
  0% {
    transform: translate(-50%, -75%) rotate(0deg);
  }

  100% {
    transform: translate(-50%, -75%) rotate(360deg);
  }
}

#send_button {
  float: right;
}
</style>

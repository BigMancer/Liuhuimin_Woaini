<template>
  <div class="write_page">
    <div class="Write">
      <keep-alive>
        <textarea
          name="write_text"
          id="write"
          cols="30"
          rows="15"
          v-model="msg"
          placeholder="我想对你说："
        ></textarea>
      </keep-alive>
      <div id="send_button">
        <button @click="send_mail">
          <span>send</span>
          <div class="liquid"></div>
        </button>
      </div>
    </div>
  </div>
</template>
<script>
import { api_send_mail } from "@/apis/api"; // 导入api
export default {
  name: "Write",
  data() {
    return {
      msg: "",
    };
  },
  methods: {
    async send_mail() {
      // 调用api接口，并传入参数
      // console.log(this.msg);
      const res = await api_send_mail({
        write_text: this.msg,
      });
      // 获取的响应结果
      if (res.code == 0) {
        alert("信件已投递");
        this.msg = "";
      } else if (res.code == 1) {
        alert(res.err);
      }
    },
  },
};
</script>
<style scoped>
.write_page {
  margin: auto;
  border-radius: 13px;
  background-color: #ffe4e1;
  opacity: 0.8;
  background-size: 22px 22px;
  background-image: repeating-linear-gradient(
    0deg,
    #fbb5c2,
    #fbb5c2 1.1px,
    #ffe4e1 1.1px,
    #ffe4e1
  );
  min-width: 300px;
  max-width: 900px;
  position: relative;
  padding-top: 20px;
  padding-left: 20px;
  padding-right: 20px;
  padding-bottom: 20px;
  text-align: left;
  border-right: 2px dotted #f78da7;
  border-left: 2px dotted #f78da7;
}

#container {
  display: inline;
}

button {
  position: relative;
  padding-top: 10px;
  padding-right: 103px;
  padding-left: 43px;
  padding-bottom: 8px;
  display: block;
  text-decoration: none;
  text-transform: uppercase;
  width: 85px;
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
#write {
  background-color: transparent;
  border: 0;
  outline: none;
  text-align: left;
  width: 100%;
  color: #000000;
  font-weight: bold;
  font-size: x-large;
  text-indent: 20px;
}
#send_button {
  float: right;
}
</style>








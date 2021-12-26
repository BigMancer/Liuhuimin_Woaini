<template>
  <div class="Read_my_story">
    <div id="markdown-view" v-html="msg"></div>
  </div>
</template>

<script>
// import { reporter } from "vfile-reporter";
import { remark } from "remark";
import remarkPresetLintMarkdownStyleGuide from "remark-preset-lint-markdown-style-guide";
import remarkHtml from "remark-html";
import { api_read_mail } from "@/apis/api";
export default {
  name: "Read_my_story",
  data() {
    return {
      msg: "# Test",
    };
  },
  async mounted() {
    const res = await api_read_mail({
      read_text: "",
      action: "read_my_story",
    });
    // 输出服务器的响应结果
    // console.log(res);
    let req_msg=''
    if (res.code == 0) {
      req_msg = res.msg;
    }
    remark().use(remarkPresetLintMarkdownStyleGuide).use(remarkHtml).process(req_msg) .then((file) => {this.msg = file;});
  },
};
</script>
<style scoped>
</style>

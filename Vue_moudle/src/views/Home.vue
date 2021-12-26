<template>
  <div class="home">
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
  name: "Read_Home",
  data() {
    return {
      msg: "",
    };
  },
  async mounted() {
    const res = await api_read_mail({
      read_text: "",
      action: "read_Home",
    });
    let req_msg=''
    if (res.code == 0) {
      req_msg = res.msg;
    }
    remark().use(remarkPresetLintMarkdownStyleGuide).use(remarkHtml).process(req_msg) .then((file) => {this.msg = file;});
  },
};
</script>



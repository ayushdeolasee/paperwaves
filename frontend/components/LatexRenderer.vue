
<template>
  <span v-html="renderedHtml"></span>
</template>

<script setup>
import { ref, watch, onMounted } from 'vue';
import katex from 'katex';
import 'katex/dist/katex.min.css';

const props = defineProps({
  content: {
    type: String,
    required: true,
  },
});

const renderedHtml = ref("");

const renderLatex = (text) => {
  if (!text) return "";
  // This regex looks for content between $...$, \(...\), and $...$
  const latexRegex = /\$\$(.*?)\$\$|\\\((.*?)\\\\\)|\$(.*?)\$/gs;
  return text.replace(latexRegex, (match, p1, p2, p3) => {
    const latex = p1 || p2 || p3;
    if (latex) {
        try {
            return katex.renderToString(latex, { throwOnError: false, displayMode: !!p1 });
        }
        catch (e) {
            console.error("KaTeX rendering error:", e);
            return match; // Return the original string if rendering fails
        }
    }
    return match;
  });
};

watch(
  () => props.content,
  (newContent) => {
    renderedHtml.value = renderLatex(newContent);
  },
  { immediate: true }
);
</script>


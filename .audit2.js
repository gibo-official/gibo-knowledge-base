const fs = require("fs");
const path = require("path");
function walk(d) {
  let r = [];
  for (const e of fs.readdirSync(d, { withFileTypes: true })) {
    const p = path.join(d, e.name);
    if ([".git", "node_modules", "tmp", "__pycache__"].includes(e.name)) continue;
    if (e.isDirectory()) r = r.concat(walk(p));
    else if (e.name.endsWith(".md")) r.push(p);
  }
  return r;
}
const FOOTER_RE = /更新日期|最后更新|版权所有|©|Updated:|Update:|Copyright/i;
const files = walk(".").filter((f) => /^(zh|en)[/\\]/.test(f));
let zhNo = [], enNo = [], total = files.length, has = 0;
for (const f of files) {
  const s = fs.readFileSync(f, "utf8");
  if (FOOTER_RE.test(s)) has++;
  else {
    if (/^zh[/\\]/.test(f)) zhNo.push(f.split("\\").join("/"));
    else enNo.push(f.split("\\").join("/"));
  }
}
console.log("内容文件总数:", total);
console.log("已有页脚:", has);
console.log("真正缺页脚:", files.length - has, "(zh:" + zhNo.length + " en:" + enNo.length + ")");
console.log("--- zh 缺页脚样本(前15) ---");
zhNo.slice(0, 15).forEach((x) => console.log("  " + x));
console.log("--- en 缺页脚样本(前15) ---");
enNo.slice(0, 15).forEach((x) => console.log("  " + x));
fs.writeFileSync(".nofooter.json", JSON.stringify({ zhNo, enNo }, null, 2));
console.log("\n已导出 .nofooter.json 供补丁脚本使用");

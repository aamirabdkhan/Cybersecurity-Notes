/*
THIS IS A GENERATED/BUNDLED FILE BY ESBUILD
if you want to view the source, please visit the github repository of this plugin
*/

"use strict";
var __defProp = Object.defineProperty;
var __getOwnPropDesc = Object.getOwnPropertyDescriptor;
var __getOwnPropNames = Object.getOwnPropertyNames;
var __hasOwnProp = Object.prototype.hasOwnProperty;
var __export = (target, all) => {
  for (var name in all)
    __defProp(target, name, { get: all[name], enumerable: true });
};
var __copyProps = (to, from, except, desc) => {
  if (from && typeof from === "object" || typeof from === "function") {
    for (let key of __getOwnPropNames(from))
      if (!__hasOwnProp.call(to, key) && key !== except)
        __defProp(to, key, { get: () => from[key], enumerable: !(desc = __getOwnPropDesc(from, key)) || desc.enumerable });
  }
  return to;
};
var __toCommonJS = (mod) => __copyProps(__defProp({}, "__esModule", { value: true }), mod);

// src/main.ts
var main_exports = {};
__export(main_exports, {
  default: () => BacklinkCachePlugin
});
module.exports = __toCommonJS(main_exports);

// node_modules/obsidian-typings/lib/obsidian/implementations/CustomArrayDictImpl.ts
var CustomArrayDictImpl = class {
  data = {};
  add(key, value) {
    if (!this.data.hasOwnProperty(key))
      this.data[key] = [];
    const values = this.data[key];
    if (!values.includes(value))
      values.push(value);
  }
  remove(key, value) {
    const values = this.data[key];
    if (!values)
      return;
    values.remove(value);
    if (values.length === 0)
      delete this.data[key];
  }
  removeKey(key) {
    delete this.data[key];
  }
  get(key) {
    return this.data.hasOwnProperty(key) ? this.data[key] : null;
  }
  keys() {
    return Object.keys(this.data);
  }
  clear(key) {
    delete this.data[key];
  }
  clearAll() {
    this.data = {};
  }
  contains(key, value) {
    const values = this.data[key];
    return values && values.contains(value) || false;
  }
  count() {
    let ans = 0;
    for (const key in this.data) {
      if (this.data.hasOwnProperty(key))
        ans += this.data[key].length;
    }
    return ans;
  }
};

// src/OriginalFunc.ts
function setOriginalFunc(func, originalFunc) {
  func.originalFunc = originalFunc;
}

// src/BacklinkCachePlugin.ts
var import_obsidian = require("obsidian");

// src/Async.ts
async function retryWithTimeout(asyncFn, {
  timeoutInMilliseconds = 5e3,
  retryDelayInMilliseconds = 100
} = {}) {
  await runWithTimeout(timeoutInMilliseconds, async () => {
    let failedBefore = false;
    while (true) {
      if (await asyncFn()) {
        if (failedBefore) {
          console.debug("Retry completed successfully");
        }
        return;
      }
      failedBefore = true;
      console.debug(`Retry completed unsuccessfully. Trying again in ${retryDelayInMilliseconds} milliseconds`);
      await delay(retryDelayInMilliseconds);
    }
  });
}
async function delay(milliseconds) {
  await new Promise((resolve) => {
    setTimeout(resolve, milliseconds);
  });
}
async function runWithTimeout(timeoutInMilliseconds, asyncFn) {
  return await Promise.race([asyncFn(), timeout()]);
  async function timeout() {
    await delay(timeoutInMilliseconds);
    throw new Error(`Timed out in ${timeoutInMilliseconds} milliseconds`);
  }
}

// src/MetadataCache.ts
async function getCacheSafe(app, fileOrPath) {
  let cache = null;
  await retryWithTimeout(async () => {
    const file = typeof fileOrPath === "string" ? app.vault.getFileByPath(fileOrPath) : fileOrPath;
    if (!file) {
      cache = null;
      return true;
    }
    await saveNote(app, file);
    const fileInfo = app.metadataCache.getFileInfo(file.path);
    const stat = await app.vault.adapter.stat(file.path);
    if (!fileInfo) {
      console.debug(`File cache info for ${file.path} is missing`);
      return false;
    } else if (!stat) {
      console.debug(`File stat for ${file.path} is missing`);
      return false;
    } else if (fileInfo.mtime < stat.mtime) {
      console.debug(`File cache info for ${file.path} is from ${new Date(fileInfo.mtime).toString()} which is older than the file modification timestamp ${new Date(stat.mtime).toString()}`);
      return false;
    } else {
      cache = app.metadataCache.getFileCache(file);
      if (!cache) {
        console.debug(`File cache for ${file.path} is missing`);
        return false;
      } else {
        return true;
      }
    }
  }, {
    timeoutInMilliseconds: 6e4
  });
  return cache;
}
async function saveNote(app, note) {
  if (note.extension.toLowerCase() !== "md") {
    return;
  }
  for (const leaf of app.workspace.getLeavesOfType("markdown")) {
    const view = leaf.view;
    if (view.file?.path === note.path) {
      await view.save();
    }
  }
}
function getAllLinks(cache) {
  let links = [];
  if (cache.links) {
    links.push(...cache.links);
  }
  if (cache.embeds) {
    links.push(...cache.embeds);
  }
  links.sort((a, b) => a.position.start.offset - b.position.start.offset);
  links = links.filter((link, index) => {
    if (index === 0) {
      return true;
    }
    return link.position.start.offset !== links[index - 1].position.start.offset;
  });
  return links;
}

// src/BacklinkCachePlugin.ts
var INTERVAL_IN_MILLISECONDS = 5e3;
var BacklinkCachePlugin = class extends import_obsidian.Plugin {
  linksMap = /* @__PURE__ */ new Map();
  backlinksMap = /* @__PURE__ */ new Map();
  pendingActions = /* @__PURE__ */ new Map();
  abortSignal;
  onload() {
    const abortController = new AbortController();
    this.register(() => abortController.abort());
    this.abortSignal = abortController.signal;
    this.app.workspace.onLayoutReady(this.onLayoutReady.bind(this));
  }
  async onLayoutReady() {
    const noteFiles = this.app.vault.getMarkdownFiles().sort((a, b) => a.path.localeCompare(b.path));
    const notice = new import_obsidian.Notice("", 0);
    let i = 0;
    for (const noteFile of noteFiles) {
      if (this.abortSignal.aborted) {
        notice.hide();
        return;
      }
      i++;
      const message = `Processing backlinks # ${i} / ${noteFiles.length} - ${noteFile.path}`;
      console.debug(message);
      notice.setMessage(message);
      await this.refreshBacklinks(noteFile.path);
    }
    notice.hide();
    const originalFunc = this.app.metadataCache.getBacklinksForFile;
    this.app.metadataCache.getBacklinksForFile = this.getBacklinksForFile.bind(this);
    setOriginalFunc(this.app.metadataCache.getBacklinksForFile, originalFunc.bind(this.app.metadataCache));
    this.registerEvent(this.app.metadataCache.on("changed", this.handleMetadataChanged.bind(this)));
    this.registerEvent(this.app.vault.on("rename", this.handleFileRename.bind(this)));
    this.registerEvent(this.app.vault.on("delete", this.handleFileDelete.bind(this)));
    this.register(() => {
      this.app.metadataCache.getBacklinksForFile = originalFunc;
    });
    this.registerInterval(window.setInterval(() => void this.processPendingActions().catch(console.error), INTERVAL_IN_MILLISECONDS));
  }
  async processPendingActions() {
    const pathActions = Array.from(this.pendingActions.entries());
    this.pendingActions.clear();
    for (const [path, action] of pathActions) {
      switch (action) {
        case 0 /* Refresh */:
          await this.refreshBacklinks(path);
          break;
        case 1 /* Remove */:
          this.removeBacklinks(path);
          break;
      }
    }
  }
  async refreshBacklinks(notePath) {
    console.debug(`Refreshing backlinks for ${notePath}`);
    this.removeLinkedPathEntries(notePath);
    const noteFile = this.app.vault.getFileByPath(notePath);
    if (!noteFile) {
      return;
    }
    if (!this.linksMap.has(notePath)) {
      this.linksMap.set(notePath, /* @__PURE__ */ new Set());
    }
    let cache;
    try {
      cache = await getCacheSafe(this.app, noteFile);
    } catch (e) {
      console.error(`Error getting cache for ${notePath}`, e);
      return;
    }
    if (!cache) {
      return;
    }
    for (const link of getAllLinks(cache)) {
      const linkFile = this.app.metadataCache.getFirstLinkpathDest(this.extractLinkPath(link.link), notePath);
      if (!linkFile) {
        continue;
      }
      let notePathLinksMap = this.backlinksMap.get(linkFile.path);
      if (!notePathLinksMap) {
        notePathLinksMap = /* @__PURE__ */ new Map();
        this.backlinksMap.set(linkFile.path, notePathLinksMap);
      }
      let linkSet = notePathLinksMap.get(notePath);
      if (!linkSet) {
        linkSet = /* @__PURE__ */ new Set();
        notePathLinksMap.set(notePath, linkSet);
      }
      linkSet.add(link);
      this.linksMap.get(notePath)?.add(linkFile.path);
    }
  }
  removeBacklinks(path) {
    console.debug(`Removing backlinks for ${path}`);
    this.removePathEntries(path);
  }
  handleMetadataChanged(file) {
    this.pendingActions.set(file.path, 0 /* Refresh */);
  }
  handleFileRename(file, oldPath) {
    this.pendingActions.set(oldPath, 1 /* Remove */);
    this.pendingActions.set(file.path, 0 /* Refresh */);
  }
  handleFileDelete(file) {
    this.pendingActions.set(file.path, 1 /* Remove */);
  }
  removePathEntries(path) {
    console.debug(`Removing ${path} entries`);
    this.backlinksMap.delete(path);
    this.removeLinkedPathEntries(path);
  }
  removeLinkedPathEntries(path) {
    const linkedNotePaths = this.linksMap.get(path) || [];
    for (const linkedNotePath of linkedNotePaths) {
      this.backlinksMap.get(linkedNotePath)?.delete(path);
    }
    this.linksMap.delete(path);
  }
  getBacklinksForFile(file) {
    const notePathLinksMap = this.backlinksMap.get(file?.path ?? "") || /* @__PURE__ */ new Map();
    const dict = new CustomArrayDictImpl();
    for (const [notePath, links] of notePathLinksMap.entries()) {
      for (const link of [...links].sort((a, b) => a.position.start.offset - b.position.start.offset)) {
        dict.add(notePath, link);
      }
    }
    return dict;
  }
  extractLinkPath(link) {
    return link.replace(/\u00A0/g, " ").normalize("NFC").split("#")[0];
  }
};

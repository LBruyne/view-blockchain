<template>
  <el-container>
    <div
      class="dialog-card"
      :style="`left: ${mousePos.x - 20}px; top: ${mousePos.y + 20}px;`"
      v-if="showDialog"
    >
      <div>
        <i class="el-icon-location-outline margin-right"></i>Address:
        {{ cutString(peers[displayPeerIndex].addr) }}
      </div>
      <div>
        <i class="el-icon-location-outline margin-right"></i>IPv4:
        {{ peers[displayPeerIndex].ipv4 }}
      </div>
      <div>
        <i class="el-icon-bank-card margin-right"></i>Balance:
        {{ peers[displayPeerIndex].balance }}
      </div>
      <div>Transactions</div>
      <el-collapse
        v-for="(tx, txIndex) in peers[displayPeerIndex].txs"
        :key="txIndex"
      >
        <el-collapse-item
          :title="
            'Transaction #' + txIndex + (tx.is_coinbase ? ' COINBASE' : '')
          "
        >
          <div class="block-collapse">
            <div>
              <div>TX IN</div>
              <el-table :data="tx.v_in" style="width: 100%">
                <el-table-column
                  prop="to_spend.pointer_tx_id"
                  label="Source"
                  width="180"
                >
                </el-table-column>
                <el-table-column
                  prop="to_spend.pointer_n"
                  label="No"
                  width="40"
                >
                </el-table-column>
              </el-table>
            </div>
            <div>
              <div>TX OUT</div>
              <el-table :data="tx.v_out" style="width: 100%">
                <el-table-column prop="to_addr" label="Target" width="180">
                </el-table-column>
                <el-table-column prop="value" label="Value" width="60">
                </el-table-column>
              </el-table>
            </div>
          </div>
        </el-collapse-item>
      </el-collapse>
    </div>

    <el-header class="bit-header" style="height: 60px; line-height: 60px">
      BlockChain Simulator
    </el-header>
    <el-container style="height: calc(100vh - 60px)">
      <el-aside width="280px" class="bit-aside">
        <div class="aside-btn-wrapper">
          <el-tooltip
            effect="dark"
            content="Click to make random transactions between peers"
            placement="right-end"
          >
            <div class="aside-btn">
              <el-button
                class="margin-right"
                icon="el-icon-document-copy"
                circle
                @click="makeRandomTX"
              ></el-button
              >Random Transactions
            </div>
          </el-tooltip>
          <el-tooltip
            effect="dark"
            content="Click to reach consensus by mining"
            placement="right-end"
          >
            <div class="aside-btn">
              <el-button
                class="margin-right"
                icon="el-icon-document-checked"
                circle
                @click="makeConsensus"
              ></el-button
              >Make Consensus
            </div>
          </el-tooltip>
          <el-tooltip
            effect="dark"
            content="Click to make one transaction"
            placement="right-end"
          >
            <div class="aside-btn">
              <el-button
                class="margin-right"
                icon="el-icon-tickets"
                circle
                @click="toggleTXTable"
              ></el-button
              >One Transaction
            </div>
          </el-tooltip>
          <div
            class="foldable-div"
            :style="`height: ${showTXTable ? '240px' : '0'};`"
          >
            <el-input
              style="margin: 10px 0"
              v-model="createTX.from"
              placeholder="From"
              ><i slot="prefix" class="el-input__icon el-icon-right"></i
            ></el-input>
            <el-input
              style="margin: 10px 0"
              v-model="createTX.to"
              placeholder="To"
              ><i slot="prefix" class="el-input__icon el-icon-back"></i
            ></el-input>
            <el-input
              style="margin: 10px 0"
              v-model="createTX.value"
              placeholder="Value"
              ><i slot="prefix" class="el-input__icon el-icon-money"></i
            ></el-input>
            <el-button
              @click="createTransaction"
              style="margin: 10px 0"
              type="primary"
              round
              >Submit Transaction</el-button
            >
          </div>
          <!-- <el-tooltip
            effect="dark"
            content="Click to make five consensus"
            placement="right-end"
          >
            <div class="aside-btn">
              <el-button
                class="margin-right"
                icon="el-icon-folder-checked"
                circle
              ></el-button
              >Make 5 Consensus
            </div>
          </el-tooltip> -->
          <el-tooltip
            effect="dark"
            content="Click to add one peer"
            placement="right-end"
          >
            <div class="aside-btn">
              <el-button
                class="margin-right"
                icon="el-icon-plus"
                circle
                @click="addPeer"
              ></el-button
              >Add One Peer
            </div>
          </el-tooltip>
        </div>

        <div class="info-card" style="text-align: left">
          <div style="font-size: 22px">Network Info</div>
          <el-divider></el-divider>
          <div>Number of peers: {{ network.peer_num }}</div>
          <div>Block Height: {{ network.block_height }}</div>
          <div>GDP: {{ network.GDP }}</div>
          <div>Local time: {{ network.local_time }}</div>
          <div>
            Current winner: {{ cutString(network.current_winner) || "Nobody" }}
          </div>
          <div>Number of txs in network: {{ network.num_of_txs }}</div>
        </div>
      </el-aside>
      <el-container>
        <!-- =========== HEADER =========== -->
        <el-main>
          <div class="component-wrapper">
            <div
              class="peer-wrapper"
              id="peer-scroll-wrapper"
              @scroll="onPeerScroll"
            >
              <div class="peer-node-wrapper">
                <div
                  :id="`peer-node-${index}`"
                  :class="
                    'peer-node' +
                    (highlightPeerNodeIndex == index ? ' highlight' : '')
                  "
                  v-for="(item, index) in peers"
                  :key="index"
                  @mouseenter="showPeerInfo(index)"
                  @mouseleave="hidePeerInfo"
                  @click="getPeerPrivateInfo(index)"
                >
                  <i class="el-icon-user-solid">#{{ index }}</i>
                </div>
              </div>
            </div>
          </div>

          <div
            id="block-scroll-wrapper"
            style="width: 100%; overflow: scroll; height: 60vh"
            @scroll="onBlockScroll"
          >
            <div class="block-card-wrapper" id="block-scroll-card-wrapper">
              <div
                :id="`block-card-${index}`"
                class="block-card"
                v-for="(item, index) in blockInfo"
                :key="index"
              >
                <div style="font-size: 22px">Block #{{ index }}</div>
                <div>Previous Hash: {{ cutString(item.previous_hash) }}</div>
                <div>Current Hash: {{ cutString(item.current_hash) }}</div>
                <!-- <div>Transactions</div> -->
                <el-collapse
                  v-model="activeBlockTXs"
                  v-for="(tx, txIndex) in item.txs"
                  :key="txIndex"
                >
                  <el-collapse-item
                    :name="tx.id"
                    :class="highlightTXID == tx.id ? 'highlight' : ''"
                    :title="
                      'Transaction #' +
                      txIndex +
                      (tx.is_coinbase ? ' COINBASE ' : ' ') +
                      'ID: ' +
                      cutString(tx.id)
                    "
                    :id="`block-tx-${tx.id}`"
                  >
                    <div class="block-collapse">
                      <div>
                        <div>TX IN</div>
                        <el-table :data="tx.v_in" style="width: 100%">
                          <el-table-column
                            prop="to_spend.pointer_tx_id_cut"
                            label="Source"
                            width="180"
                          >
                          </el-table-column>
                          <el-table-column
                            prop="to_spend.pointer_n"
                            label="No"
                            width="40"
                          >
                          </el-table-column>
                        </el-table>
                      </div>
                      <div>
                        <div>TX OUT</div>
                        <el-table :data="tx.v_out" style="width: 100%">
                          <el-table-column label="Target" width="180">
                            <template slot-scope="scope">
                              <div
                                @click="
                                  highlightPeerNode(
                                    tx.id,
                                    scope.$index,
                                    scope.row.to_addr
                                  )
                                "
                                :id="`block-tx-${tx.id}-row-${scope.$index}`"
                                :class="
                                  'tx-row ' +
                                  (highlightTXID == tx.id &&
                                  highlightTXROW == scope.$index
                                    ? 'highlight'
                                    : '')
                                "
                              >
                                {{ scope.row.to_addr_cut }}
                              </div>
                            </template>
                          </el-table-column>
                          <el-table-column
                            prop="value"
                            label="Value"
                            width="60"
                          >
                          </el-table-column>
                        </el-table>
                      </div>
                    </div>
                  </el-collapse-item>
                </el-collapse>
              </div>
              <div style="min-width: 40px"></div>
            </div>
          </div>
        </el-main>
        <!-- =========== FOOTER =========== -->
        <el-footer class="bit-footer" height="60px">
          BlockChain Simulator | SRTP 2021
        </el-footer>
      </el-container>
      <el-aside width="280px" class="bit-aside">
        <div class="subtitle">Peer Info</div>
        <div>
          <div>
            <i class="el-icon-user-solid"></i>#{{ detailInfo.basic.id }}
          </div>
          <div>
            Public Key: {{ cutString(detailInfo.basic.public_key || "") }}
          </div>
          <div>
            Private Key: {{ cutString(detailInfo.basic.secret_key || "") }}
          </div>
        </div>

        <div class="subtitle">Unconfirmed UTXOs</div>
        <div
          class="utxo-card"
          v-if="!detailInfo.unconfirm || !detailInfo.unconfirm.length"
        >
          No Record
        </div>
        <div
          class="utxo-card"
          v-for="(item, index) in detailInfo.unconfirm"
          :key="item.tx_id"
          style="text-align: left"
        >
          <div>TX #{{ index }}</div>
          <div
            style="cursor: pointer"
            @click="highlightTransactionNode(item.tx_id)"
          >
            TX id: {{ cutString(item.tx_id) }}
          </div>
          <div
            style="cursor: pointer"
            @click="highlightTransactionRow(item.tx_id, item.tx_vout_n)"
          >
            TX No: {{ item.tx_vout_n }}
          </div>
          <div>TX Value: {{ item.vout_value }}</div>
        </div>
        <div class="subtitle">Confirmed UTXOs</div>
        <div
          class="utxo-card"
          v-if="!detailInfo.confirm || !detailInfo.confirm.length"
        >
          No Record
        </div>
        <div
          class="utxo-card"
          v-for="(item, index) in detailInfo.confirm"
          :key="item.tx_id"
          style="text-align: left"
        >
          <div>TX #{{ index }}</div>
          <div
            style="cursor: pointer"
            @click="highlightTransactionNode(item.tx_id)"
          >
            TX id: {{ cutString(item.tx_id) }}
          </div>
          <div
            style="cursor: pointer"
            @click="highlightTransactionRow(item.tx_id, item.tx_vout_n)"
          >
            TX No: {{ item.tx_vout_n }}
          </div>
          <div>TX Value: {{ item.vout_value }}</div>
        </div>

        <div class="subtitle">Mem Pool</div>
        <div
          class="utxo-card"
          v-if="!detailInfo.basic.mem_pool || !detailInfo.basic.mem_pool.length"
        >
          No Record
        </div>
        <div
          class="utxo-card"
          v-for="(item, index) in detailInfo.basic.mem_pool"
          :key="item.tx_id"
          style="text-align: left"
        >
          <div>TX #{{ index }}</div>
          <div>TX id: {{ cutString(item.id) }}</div>
          <div>TX No: {{ item.fee }}</div>
          <div style="color: teal">
            More Info will be Shown As the Tx is written into Block (After
            Making Consensus)
          </div>
        </div>
      </el-aside>
    </el-container>
  </el-container>
</template>

<script>
export default {
  name: "BlockChain",
  props: {},
  data: () => {
    return {
      mousePos: { x: 0, y: 0 },
      displayPeerIndex: 0,
      showDialog: false,
      peers: [],
      createTX: { from: "", to: "", value: 0 },
      showTXTable: false,
      network: {},
      consoleOutput: [],
      blockInfo: [],
      detailInfo: {
        basic: {},
        confirm: {},
        unconfirm: {},
      },
      highlightPeerNodeIndex: -1,
      highlightTXID: "",
      highlightTXROW: -1,
      activeBlockTXs: [],
    };
  },
  async created() {
    let networkReq = await this.$http({
      method: "get",
      url: "/network/detail",
      crossdomain: true,
    });
    this.$data.network = networkReq.data.data;

    document.onmousemove = () => {
      var e = window.event;
      this.$data.mousePos = { x: e.clientX, y: e.clientY };
    };

    this.getPeerList();
    this.getBlockInfo();
  },
  mounted() {
    this.blockScrollWrapper = document.getElementById("block-scroll-wrapper");
    this.peerScrollWrapper = document.getElementById("peer-scroll-wrapper");
  },

  methods: {
    async getPeerList() {
      let res = await this.$http({
        method: "get",
        url: "/network/peer/list",
        crossdomain: true,
      });
      console.log(res.data.data);
      this.$data.peers = res.data.data;
    },
    async createTransaction() {
      var that = this;
      let res = await this.$http({
        method: "post",
        url: "/network/transaction/create",
        data: {
          transaction_originator_id: this.$data.createTX.from,
          transaction_receipt_id: this.$data.createTX.to,
          transaction_price: this.$data.createTX.value,
        },
        crossdomain: true,
      });
      this.$data.showTXTable = false;
      this.$data.createTX = { from: "", to: "", value: 0 };
      const h = this.$createElement;
      this.$message({
        message: h("p", null, [
          h(
            "p",
            { style: "color: teal" },
            `Success! Following are the Brief Info`
          ),
          h("p", null, `transaction_id: ${that.cutString(res.data.data.id)}`),
          h("p", null, `transaction_fee: ${res.data.data.fee}`),
          h("p", null, `sender_ip: ${res.data.data.sender.ip}`),
          h("p", null, `receiver_ip: ${res.data.data.receiver.ip}`),
          h(
            "p",
            { style: "color: teal" },
            `More Info Could Be See In the Mem Pool`
          ),
        ]),
        type: "success",
        showClose: true,
        duration: 6000,
      });
      console.log(res);
    },
    async addPeer() {
      await this.$http({
        method: "get",
        url: "/network/peer/add",
        crossdomain: true,
      });
      this.getPeerList();
    },
    async getBlockInfo() {
      let res = await this.$http({
        method: "get",
        url: "/network/blockchain/list",
        crossdomain: true,
      });
      console.log("getBlockInfo", res);
      res.data.data.forEach((blockItem) => {
        blockItem.txs.forEach((txItem) => {
          txItem.v_out.forEach((outItem) => {
            outItem.to_addr_cut = this.cutString(outItem.to_addr);
          });
          if (!txItem.is_coinbase) {
            txItem.v_in.forEach((inItem) => {
              inItem.to_spend.pointer_tx_id_cut = this.cutString(
                inItem.to_spend.pointer_tx_id
              );
            });
          } else {
            txItem.v_in = [
              {
                to_spend: {
                  pointer_tx_id_cut: "Mining Gain",
                  pointer_n: "--",
                },
              },
            ];
          }
        });
      });
      this.$data.blockInfo = res.data.data;
    },
    async makeRandomTX() {
      var that = this;
      let res = await this.$http({
        method: "get",
        url: "/network/transaction/random",
        crossdomain: true,
      });
      const h = this.$createElement;
      this.$message({
        message: h("p", null, [
          h(
            "p",
            { style: "color: teal" },
            `Success! Following are the Brief Info`
          ),
          h("p", null, `transaction_id: ${that.cutString(res.data.data.id)}`),
          h("p", null, `transaction_fee: ${res.data.data.fee}`),
          h(
            "p",
            null,
            `sender: peer(ip:${res.data.data.sender.ip})(pid=${res.data.data.sender.pid})`
          ),
          h(
            "p",
            null,
            `receiver: peer(ip:${res.data.data.receiver.ip})(pid=${res.data.data.receiver.pid})`
          ),
          h(
            "p",
            { style: "color: teal" },
            `More Info Could Be See In the Mem Pool`
          ),
        ]),
        type: "success",
        showClose: true,
        duration: 6000,
      });
      this.getBlockInfo();
    },
    async makeConsensus() {
      var that = this;
      const loading = this.$loading({
        lock: true,
        text: `${parseInt(
          Math.random() * that.$data.peers.length
        )} Peers Are Mining,Please Wait About 10s`,
        spinner: "el-icon-loading",
        background: "rgba(0, 0, 0, 0.8)",
      });

      let res = await this.$http({
        method: "get",
        url: "/network/consensus",
        crossdomain: true,
      });
      if (res.data.data.result == false) {
        const h = this.$createElement;
        this.$message({
          message: h("p", null, [
            h("p", { style: "color: teal" }, `Using POW Method`),
            h(
              "p",
              { style: "color: teal" },
              `Don't have enough Txs for Txs Block`
            ),
            h(
              "p",
              { style: "color: teal" },
              `The Block wasn't received By Any One`
            ),
          ]),
          type: "warning",
          showClose: true,
          duration: 6000,
        });
      } else {
        const h = this.$createElement;
        this.$message({
          message: h("p", null, [
            h("p", { style: "color: teal" }, `Using POW Method`),
            h("p", { style: "color: teal" }, `${res.data.data.logInfo[1]}`),
            h("p", { style: "color: teal" }, `${res.data.data.logInfo[2]}`),
          ]),
          type: "success",
          showClose: true,
          duration: 6000,
        });
        console.log("res", res.data.data);
      }
      this.getBlockInfo();
      loading.close();
    },
    async getPeerPrivateInfo(id) {
      let res = await this.$http({
        method: "get",
        url: `/network/peer/more?pid=${id}`,
        crossdomain: true,
      });
      console.log("detail", res);
      this.$data.detailInfo.basic = res.data.data;

      res = await this.$http({
        method: "get",
        url: `/network/peer/utxo/unconfirm?peer_id=${id}`,
        crossdomain: true,
      });
      this.$data.detailInfo.unconfirm = res.data.data;

      res = await this.$http({
        method: "get",
        url: `/network/peer/utxo/confirm?peer_id=${id}`,
        crossdomain: true,
      });
      this.$data.detailInfo.confirm = res.data.data;
    },
    showPeerInfo(id) {
      this.$data.displayPeerIndex = id;
      this.$data.showDialog = true;
    },
    hidePeerInfo() {
      this.$data.showDialog = false;
    },
    toggleTXTable() {
      this.$data.showTXTable = !this.$data.showTXTable;
      console.log(this.$data);
    },
    cutString(str, n1 = 4, n2 = 6) {
      if (!str) return "";
      var len = str.length;
      if (len < 2 * n1) {
        return str;
      } else {
        var ec = "";
        for (var i = 0; i < n2; i++) {
          ec = ec + ".";
        }
        return `${str.substr(0, n1)}` + ec + `${str.substr(len - n1, n1)}`;
      }
    },
    onBlockScroll() {},
    onPeerScroll() {},
    highlightPeerNode(txId, txRow, peerAddr) {
      let targetPeerIndex = -1;
      this.peers.forEach((item, index) => {
        if (item.addr == peerAddr) targetPeerIndex = index;
      });
      let targetScrollLeft =
        document.getElementById(`peer-node-${targetPeerIndex}`).offsetLeft -
        this.peerScrollWrapper.offsetLeft;
      this.peerScrollWrapper.scrollLeft = targetScrollLeft;
      this.$data.highlightPeerNodeIndex = targetPeerIndex;
      this.getPeerPrivateInfo(targetPeerIndex);
      this.$data.displayPeerIndex = targetPeerIndex;
      this.$data.highlightTXID = txId;
      this.$data.highlightTXROW = txRow;
    },
    highlightTransactionNode(txId) {
      console.log("highlightTransactionNode");
      let targetNode = document
        .getElementById(`block-tx-${txId}`)
        .getBoundingClientRect();
      let wrapperNode = this.blockScrollWrapper.getBoundingClientRect();
      let targetScrollLeft = targetNode.left - wrapperNode.left;
      let targetScrollTop = targetNode.top - wrapperNode.top;
      this.blockScrollWrapper.scrollLeft = targetScrollLeft;
      this.blockScrollWrapper.scrollTop = targetScrollTop;
      this.$data.highlightTXID = txId;
    },
    highlightTransactionRow(txId, txRow) {
      console.log("highlightTransactionRow");
      this.$data.activeBlockTXs = [txId];
      setTimeout(() => {
        let targetNode = document
          .getElementById(`block-tx-${txId}-row-${txRow}`)
          .getBoundingClientRect();
        let wrapperNode = this.blockScrollWrapper.getBoundingClientRect();
        let targetScrollLeft = targetNode.left - wrapperNode.left;
        let targetScrollTop = targetNode.top - wrapperNode.top;
        this.blockScrollWrapper.scrollLeft = targetScrollLeft;
        this.blockScrollWrapper.scrollTop = targetScrollTop;
        this.$data.highlightTXID = txId;
        this.$data.highlightTXROW = txRow;
      }, 500);
    },
  },
};
</script>

<style>
@import url("./main.css");

.highlight .el-collapse-item__header {
  background: rgba(0, 0, 0, 0.1);
}
.tx-row.highlight {
  background: rgba(0, 0, 0, 0.1);
}
.el-icon-caret-right {
  color: #409eff;
}
</style>

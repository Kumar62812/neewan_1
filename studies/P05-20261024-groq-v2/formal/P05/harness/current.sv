// SPDX-License-Identifier: MIT
`ifndef DUT
`define DUT response_b
`endif
module harness;
 (* anyseq *) reg clk, rst, req;
 wire ack, seen_reset;
`ifdef POST_RESET
 wire check_enable=seen_reset;
`else
 wire check_enable=1'b1;
`endif
 `DUT dut(.clk(clk),.rst(rst),.req(req),.ack(ack));
 p05_environment env(clk,rst,req,seen_reset);
`ifdef I1
 p05_i1_contract contract(clk,rst,req,ack,check_enable);
`endif
`ifdef I2
 p05_i2_contract contract(clk,rst,req,ack,check_enable);
`endif
`ifdef DISTINCTION
 wire ack_i2;
 response_a other(clk,rst,req,ack_i2);
 always @($global_clock) begin
  if(seen_reset) same_observation: assert(ack == ack_i2);
  c_i2_earlier: cover(seen_reset && ack_i2 && !ack);
  c_i1_later: cover(seen_reset && ack && !ack_i2);
 end
`else
 always @($global_clock) begin
  c_ack: cover(seen_reset && ack);
  c_request: cover(seen_reset && req && !rst && clk);
 end
`endif
`ifdef SELF
 wire ack_copy;
 `DUT duplicate(.clk(clk),.rst(rst),.req(req),.ack(ack_copy));
 always @($global_clock) if(seen_reset) self_equal: assert(ack == ack_copy);
`endif
endmodule

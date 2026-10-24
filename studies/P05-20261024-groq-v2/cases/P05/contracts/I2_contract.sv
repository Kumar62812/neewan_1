// SPDX-License-Identifier: MIT
module p05_i2_contract(input wire clk, rst, req, ack, enabled);
 reg valid=0;
 always @($global_clock) begin
  valid <= 1;
  if (valid && enabled) begin
   if (!$past(clk) && clk)
    i2_transfer: assert(ack == ($past(rst) ? 1'b0 : $past(req)));
   else i2_hold: assert(ack == $past(ack));
  end
 end
endmodule

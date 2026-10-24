// SPDX-License-Identifier: MIT
// Post-update contract; global steps are observation instants, not active edges.
module p05_i1_contract(input wire clk, rst, req, ack, enabled);
 reg valid=0, edge_seen=0;
 reg pending;
 always @(posedge clk) pending <= rst ? 1'b0 : req;
 always @($global_clock) begin
  valid <= 1;
  if(valid && !$past(clk) && clk) edge_seen <= 1;
  if (valid && enabled) begin
   if (!$past(clk) && clk) begin
    // The first non-reset edge may expose unspecified initial pending.
    if ($past(rst)) i1_reset: assert(ack == 0);
    else if ($past(edge_seen)) i1_transfer: assert(ack == $past(pending));
   end else i1_hold: assert(ack == $past(ack));
  end
 end
endmodule

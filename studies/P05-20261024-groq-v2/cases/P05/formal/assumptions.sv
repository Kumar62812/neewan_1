// SPDX-License-Identifier: MIT
module p05_environment(input wire clk, rst, req, output reg seen_reset=0);
 reg valid=0, edge_seen=0, last_req;
 always @($global_clock) begin
  valid <= 1;
  if (!valid) initial_clock_low: assume(!clk);
  if (valid && !$past(clk) && clk) begin
   stable_reset: assume(rst == $past(rst));
   stable_request: assume(req == $past(req));
   if (!$past(rst) && edge_seen) isolated_requests: assume(!(last_req && $past(req)));
   last_req <= $past(rst) ? 1'b0 : $past(req);
   edge_seen <= 1;
   if ($past(rst)) seen_reset <= 1;
  end
 end
endmodule

// SPDX-License-Identifier: MIT
// Current compositional state check for the unchanged reference response_b.
module p05_b_properties(input wire clk,rst,req,ack,pending);
 reg valid=0;
 always @($global_clock) begin
  valid<=1;
  if(valid) begin
   if(!$past(clk)&&clk) begin
    b_pending: assert(pending == ($past(rst)?0:$past(req)));
    b_response: assert(ack == ($past(rst)?0:$past(pending)));
   end else begin
    b_pending_hold: assert(pending==$past(pending));
    b_ack_hold: assert(ack==$past(ack));
   end
  end
 end
endmodule

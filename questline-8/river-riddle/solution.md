# River Riddle

**Initial side:** Farmer, Wolf, Goat, Cabbage  
**Goal:** Move everyone safely to the other side.

## Safe sequence of crossings(steps):

1. Farmer takes **Goat** across.  
   - Left: Wolf, Cabbage  
   - Right: Farmer, Goat

2. Farmer returns alone.  
   - Left: Farmer, Wolf, Cabbage  
   - Right: Goat

3. Farmer takes **Wolf** across.  
   - Left: Cabbage  
   - Right: Farmer, Wolf, Goat

4. Farmer brings **Goat** back.  
   - Left: Goat, Cabbage  
   - Right: Farmer, Wolf

5. Farmer takes **Cabbage** across.  
   - Left: Goat  
   - Right: Farmer, Wolf, Cabbage

6. Farmer returns alone.  
   - Left: Farmer, Goat  
   - Right: Wolf, Cabbage

7. Farmer takes **Goat** across.  
   - Left: (empty)  
   - Right: Farmer, Wolf, Goat, Cabbage — all safe!

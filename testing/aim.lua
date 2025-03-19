-- Self-injection bootstrap
local function attemptSelfInjection()
    -- Check if we're already in an exploited environment
    local isInjected = pcall(function() return Drawing ~= nil end)
    if isInjected then
        print("Environment already exploited, proceeding with aimbot...")
        return true
    end
    
    -- Try common exploit global hooks
    local exploitFunctions = {
        "syn_exec", "KRNL_LOADED", "sirhurt", "sentinel", 
        "protosmasher", "ScriptWare", "hookfunction"
    }
    
    for _, func in pairs(exploitFunctions) do
        if getgenv and getgenv()[func] then
            print("Detected exploit environment: " .. func)
            return true
        end
    end
    
    -- Check for exploit-specific APIs
    if (syn and syn.request) or (http and http.request) or request or fluxus then
        print("Exploit API detected, environment is ready")
        return true
    end
    
    -- Attempt to bootstrap an injection if possible
    local success = false
    
    -- Try to get core scripts (which would only be possible with exploit privileges)
    pcall(function()
        if gethui or get_hidden_gui then
            success = true
            print("Hidden UI access detected, environment is exploited")
        end
    end)
    
    -- Try filesystem access (only possible in exploited environment)
    pcall(function()
        if readfile or isfile then
            success = true
            print("Filesystem access detected, environment is exploited")
        end
    end)
    
    return success
end

-- Check if we're in an exploitable environment
local canRun = attemptSelfInjection()

if not canRun then
    warn("This script requires an executor to run.")
    warn("Please use a Roblox script executor like Synapse X, Krnl, etc.")
    warn("This script cannot self-inject into Roblox.")
    return
end

-- The rest of the script runs only if we're in an exploited environment
-- Wrap in pcall to catch errors during injection
local success, errorMsg = pcall(function()
    local Aimbot = {}

    -- Configuration
    Aimbot.Settings = {
        Enabled = false,
        TeamCheck = true,    -- Don't target teammates
        VisibilityCheck = true, -- Check if target is visible
        TargetPart = "Head", -- Part to aim at (Head, Torso, etc.)
        FOV = 250,           -- Field of view for targeting
        Smoothness = 0.5,    -- Lower = faster aim (0-1)
        KeyBind = Enum.KeyCode.E, -- Key to toggle aimbot
        FOVCircle = {        -- FOV visual settings
            Visible = true,
            Color = Color3.fromRGB(255, 255, 255),
            Transparency = 0.7,
            Thickness = 1
        }
    }

    -- Services
    local Players = game:GetService("Players")
    local RunService = game:GetService("RunService")
    local UserInputService = game:GetService("UserInputService")
    local Camera = workspace.CurrentCamera

    -- Variables
    local LocalPlayer = Players.LocalPlayer
    local Mouse = LocalPlayer:GetMouse()
    local FOVCircle = Drawing.new("Circle")

    -- Initialize the FOV circle
    function Aimbot:InitFOVCircle()
        FOVCircle.Visible = self.Settings.FOVCircle.Visible
        FOVCircle.Color = self.Settings.FOVCircle.Color
        FOVCircle.Thickness = self.Settings.FOVCircle.Thickness
        FOVCircle.Transparency = self.Settings.FOVCircle.Transparency
        FOVCircle.NumSides = 64
        FOVCircle.Radius = self.Settings.FOV
        FOVCircle.Filled = false
    end

    -- Update FOV circle position
    function Aimbot:UpdateFOVCircle()
        if FOVCircle then
            FOVCircle.Position = Vector2.new(Mouse.X, Mouse.Y + 36)
            FOVCircle.Radius = self.Settings.FOV
            FOVCircle.Visible = self.Settings.Enabled and self.Settings.FOVCircle.Visible
        end
    end

    -- Check if a player is valid target
    function Aimbot:IsValidTarget(player)
        if not player or not player.Character or not player.Character:FindFirstChild("Humanoid") then
            return false
        end
        
        if player.Character.Humanoid.Health <= 0 then
            return false
        end
        
        if self.Settings.TeamCheck and player.Team == LocalPlayer.Team then
            return false
        end

        local targetPart = player.Character:FindFirstChild(self.Settings.TargetPart)
        if not targetPart then
            return false
        end
        
        if self.Settings.VisibilityCheck then
            local ray = Ray.new(Camera.CFrame.Position, (targetPart.Position - Camera.CFrame.Position).Unit * 500)
            local hit, _ = workspace:FindPartOnRayWithIgnoreList(ray, {LocalPlayer.Character, Camera})
            if hit and not hit:IsDescendantOf(player.Character) then
                return false
            end
        end
        
        return true
    end

    -- Get closest player within FOV
    function Aimbot:GetClosestPlayerInFOV()
        local closestPlayer = nil
        local shortestDistance = self.Settings.FOV
        
        for _, player in pairs(Players:GetPlayers()) do
            if player ~= LocalPlayer and self:IsValidTarget(player) then
                local targetPart = player.Character:FindFirstChild(self.Settings.TargetPart)
                if targetPart then
                    local screenPoint, onScreen = Camera:WorldToScreenPoint(targetPart.Position)
                    if onScreen then
                        local distanceFromMouse = (Vector2.new(screenPoint.X, screenPoint.Y) - Vector2.new(Mouse.X, Mouse.Y)).Magnitude
                        if distanceFromMouse < shortestDistance then
                            closestPlayer = player
                            shortestDistance = distanceFromMouse
                        end
                    end
                end
            end
        end
        
        return closestPlayer
    end

    -- Aim at target
    function Aimbot:AimAtTarget(target)
        if not target or not target.Character then return end
        
        local targetPart = target.Character:FindFirstChild(self.Settings.TargetPart)
        if not targetPart then return end
        
        local targetPosition = targetPart.Position
        local cameraPosition = Camera.CFrame.Position
        
        local aimCFrame = CFrame.new(cameraPosition, targetPosition)
        Camera.CFrame = Camera.CFrame:Lerp(aimCFrame, self.Settings.Smoothness)
    end

    -- Toggle aimbot on/off
    function Aimbot:Toggle()
        self.Settings.Enabled = not self.Settings.Enabled
        print("Aimbot: " .. (self.Settings.Enabled and "Enabled" or "Disabled"))
    end

    -- Setup key bindings
    function Aimbot:SetupBindings()
        UserInputService.InputBegan:Connect(function(input, gameProcessed)
            if not gameProcessed and input.KeyCode == self.Settings.KeyBind then
                self:Toggle()
            end
        end)
    end

    -- Main loop
    function Aimbot:Start()
        -- Create a UI notification to show the script is active
        local screenGui = Instance.new("ScreenGui")
        if syn and syn.protect_gui then
            syn.protect_gui(screenGui)
        end
        
        if gethui then
            screenGui.Parent = gethui()
        elseif not game:GetService("CoreGui"):FindFirstChild("RobloxGui") then
            screenGui.Parent = game:GetService("CoreGui")
        else
            screenGui.Parent = game:GetService("Players").LocalPlayer:WaitForChild("PlayerGui")
        end
        
        local frame = Instance.new("Frame")
        frame.Size = UDim2.new(0, 200, 0, 30)
        frame.Position = UDim2.new(0.5, -100, 0, 0)
        frame.BackgroundColor3 = Color3.fromRGB(25, 25, 25)
        frame.BackgroundTransparency = 0.5
        frame.BorderSizePixel = 0
        frame.Parent = screenGui
        
        local text = Instance.new("TextLabel")
        text.Size = UDim2.new(1, 0, 1, 0)
        text.Text = "Aimbot Loaded - Press " .. self.Settings.KeyBind.Name .. " to toggle"
        text.TextColor3 = Color3.fromRGB(255, 255, 255)
        text.BackgroundTransparency = 1
        text.Parent = frame
        
        -- Make notification disappear after 5 seconds
        spawn(function()
            wait(5)
            screenGui:Destroy()
        end)
        
        self:InitFOVCircle()
        self:SetupBindings()
        
        -- Add a connection variable to allow proper cleanup on script re-execution
        self.RenderConnection = RunService.RenderStepped:Connect(function()
            self:UpdateFOVCircle()
            
            if self.Settings.Enabled then
                local target = self:GetClosestPlayerInFOV()
                if target then
                    self:AimAtTarget(target)
                end
            end
        end)
        
        print("Aimbot initialized! Press " .. self.Settings.KeyBind.Name .. " to toggle.")
    end

    -- Clean up
    function Aimbot:Destroy()
        if FOVCircle then 
            FOVCircle:Remove()
        end
        if self.RenderConnection then
            self.RenderConnection:Disconnect()
        end
        print("Aimbot cleaned up!")
    end

    -- Check if previous instance exists and destroy it (for re-execution)
    if _G.CurrentAimbot then
        _G.CurrentAimbot:Destroy()
    end

    -- Store current instance globally
    _G.CurrentAimbot = Aimbot

    -- Initialize the aimbot
    Aimbot:Start()

    return Aimbot
end)

-- Display any errors that occurred during execution
if not success then
    warn("Aimbot Error: " .. tostring(errorMsg))
end
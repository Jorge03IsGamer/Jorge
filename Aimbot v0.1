local Players = game:GetService("Players")
local RunService = game:GetService("RunService")
local TweenService = game:GetService("TweenService")
local LocalPlayer = Players.LocalPlayer
local Camera = workspace.CurrentCamera

-- Tween function for smooth size/color changes
local function tweenProperty(instance, property, goalValue, time)
    local tweenInfo = TweenInfo.new(time, Enum.EasingStyle.Quad, Enum.EasingDirection.Out)
    local tween = TweenService:Create(instance, tweenInfo, {[property] = goalValue})
    tween:Play()
end

-- Function to create health + username + distance display + health bar
local function createHealthDisplay(character, player)
    if character and character:FindFirstChild("Head") and not character.Head:FindFirstChild("HealthDisplay") then
        local billboard = Instance.new("BillboardGui")
        billboard.Name = "HealthDisplay"
        billboard.Adornee = character.Head
        billboard.Size = UDim2.new(0, 220, 0, 70) -- bigger height
        billboard.AlwaysOnTop = true
        billboard.StudsOffset = Vector3.new(0, 2.5, 0.5) -- move slightly up and forward

        -- Health bar background (on top)
        local barBackground = Instance.new("Frame")
        barBackground.Size = UDim2.new(1, 0, 0.25, 0) -- taller
        barBackground.Position = UDim2.new(0, 0, -0.35, 0) -- more above text
        barBackground.BackgroundColor3 = Color3.fromRGB(50,50,50)
        barBackground.BorderSizePixel = 0
        barBackground.Parent = billboard

        -- Health bar fill
        local barFill = Instance.new("Frame")
        barFill.Size = UDim2.new(1, 0, 1, 0)
        barFill.Position = UDim2.new(0, 0, 0, 0)
        barFill.BackgroundColor3 = Color3.fromRGB(0,255,0)
        barFill.BorderSizePixel = 0
        barFill.Parent = barBackground

        -- Username + health + distance text
        local textLabel = Instance.new("TextLabel")
        textLabel.Size = UDim2.new(1, 0, 0.6, 0)
        textLabel.Position = UDim2.new(0, 0, 0.25, 0)
        textLabel.BackgroundTransparency = 1
        textLabel.TextColor3 = Color3.new(0, 1, 0)
        textLabel.TextStrokeTransparency = 0
        textLabel.Font = Enum.Font.SourceSansBold
        textLabel.TextScaled = true
        textLabel.Parent = billboard

        billboard.Parent = character.Head

        local humanoid = character:FindFirstChildOfClass("Humanoid")
        local highlight = character:FindFirstChild("ESP")

        if humanoid then
            local lastPercent = humanoid.Health / humanoid.MaxHealth
            local pulseDirection = 1

            local function updateHealth()
                if not humanoid or humanoid.Health < 0 then return end

                local current = math.floor(humanoid.Health)
                local max = math.floor(humanoid.MaxHealth)
                local distance = math.floor((character.Head.Position - Camera.CFrame.Position).Magnitude)
                textLabel.Text = player.Name .. " " .. current .. "/" .. max .. " (" .. distance .. " studs)"

                local percent = current / max
                local textColor, fillColor, outlineColor

                if percent > 0.7 then
                    textColor = Color3.new(0,1,0) -- green
                    fillColor = Color3.fromRGB(0,255,0)
                    outlineColor = Color3.fromRGB(0,255,0)
                elseif percent > 0.55 then
                    textColor = Color3.new(1,1,0) -- yellow
                    fillColor = Color3.fromRGB(255,255,0)
                    outlineColor = Color3.fromRGB(255,255,0)
                elseif percent > 0.3 then
                    textColor = Color3.fromRGB(255,165,0) -- orange
                    fillColor = Color3.fromRGB(255,165,0)
                    outlineColor = Color3.fromRGB(255,165,0)
                else
                    textColor = Color3.new(1,0,0) -- red
                    fillColor = Color3.new(1,0,0)
                    outlineColor = Color3.fromRGB(255,0,0)
                end

                -- Update text color
                textLabel.TextColor3 = textColor

                -- Smooth health bar size
                tweenProperty(barFill, "Size", UDim2.new(percent, 0, 1, 0), 0.2)

                -- Smooth health bar color
                tweenProperty(barFill, "BackgroundColor3", fillColor, 0.2)

                -- Update ESP color
                if highlight then
                    highlight.FillColor = fillColor
                    highlight.OutlineColor = outlineColor
                end

                -- Pulse effect if low health
                if percent <= 0.3 then
                    local pulseAmount = 0.1
                    pulseDirection = pulseDirection * -1
                    local newSize = UDim2.new(percent + pulseAmount * pulseDirection, 0, 1, 0)
                    tweenProperty(barFill, "Size", newSize, 0.1)
                end

                lastPercent = percent
            end

            humanoid.HealthChanged:Connect(updateHealth)
            RunService.RenderStepped:Connect(updateHealth)
            updateHealth()
        end
    end
end

-- Function to add ESP
local function addESP(character)
    if character:FindFirstChild("ESP") then
        character.ESP:Destroy()
    end

    local highlight = Instance.new("Highlight")
    highlight.Name = "ESP"
    highlight.Adornee = character
    highlight.FillColor = Color3.fromRGB(0, 255, 0)
    highlight.OutlineColor = Color3.fromRGB(0, 255, 0)
    highlight.DepthMode = Enum.HighlightDepthMode.AlwaysOnTop
    highlight.Parent = character
end

-- Handle players
local function setupPlayer(player)
    if player ~= LocalPlayer then
        player.CharacterAdded:Connect(function(character)
            character:WaitForChild("Head")
            addESP(character)
            createHealthDisplay(character, player)
        end)

        if player.Character then
            addESP(player.Character)
            createHealthDisplay(player.Character, player)
        end
    end
end

for _, player in pairs(Players:GetPlayers()) do
    setupPlayer(player)
end

Players.PlayerAdded:Connect(setupPlayer)

-- Visibility check
local raycastParams = RaycastParams.new()
raycastParams.FilterType = Enum.RaycastFilterType.Blacklist
raycastParams.IgnoreWater = true

local function isVisible(head)
    if not head or not head.Parent then return false end
    raycastParams.FilterDescendantsInstances = {LocalPlayer.Character}
    local origin = Camera.CFrame.Position
    local direction = head.Position - origin
    local result = workspace:Raycast(origin, direction, raycastParams)
    return (not result) or (result.Instance and result.Instance:IsDescendantOf(head.Parent))
end

-- Get nearest visible player
local function getNearestVisiblePlayer()
    local nearest = nil
    local shortestDistance = math.huge
    local camPos = Camera.CFrame.Position

    for _, player in pairs(Players:GetPlayers()) do
        if player ~= LocalPlayer and player.Character and player.Character:FindFirstChild("Head") then
            local head = player.Character.Head
            local humanoid = player.Character:FindFirstChildOfClass("Humanoid")
            if humanoid and humanoid.Health > 0 and isVisible(head) then
                local distance = (head.Position - camPos).Magnitude
                if distance < shortestDistance then
                    shortestDistance = distance
                    nearest = head
                end
            end
        end
    end

    return nearest
end

-- Lock camera to nearest visible player
RunService.RenderStepped:Connect(function()
    local target = getNearestVisiblePlayer()
    if target then
        Camera.CFrame = CFrame.new(Camera.CFrame.Position, target.Position)
    end
end)
